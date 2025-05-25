import asyncio

from playwright.async_api import async_playwright

stealth_js = """
Object.defineProperty(navigator, 'webdriver', { get: () => false });

window.chrome = {
    runtime: {},
    loadTimes: undefined,
    csi: undefined
};

Object.defineProperty(navigator, 'languages', {
    get: () => ['ru-RU', 'ru', 'en-US']
});

Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5]
});

Object.defineProperty(navigator, 'hardwareConcurrency', {
    get: () => 8
});

Object.defineProperty(navigator, 'deviceMemory', {
    get: () => 8
});

Object.defineProperty(navigator, 'platform', {
    get: () => 'Win32'
});

Object.defineProperty(navigator, 'maxTouchPoints', {
    get: () => 1
});

const getParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
    if (parameter === 37445) return 'Intel Inc.';
    if (parameter === 37446) return 'Intel Iris OpenGL Engine';
    return getParameter(parameter);
};

console.debug = () => {};

const originalQuery = window.navigator.permissions.query;
window.navigator.permissions.query = (parameters) => (
    parameters.name === 'notifications'
        ? Promise.resolve({ state: Notification.permission })
        : originalQuery(parameters)
);

Object.defineProperty(navigator, 'connection', {
    get: () => ({
        rtt: 50,
        downlink: 10,
        effectiveType: '4g',
        saveData: false
    })
});
"""


async def extract_price(page):
    selectors = ('span.m1q_28.qm1_28.q5m_28', 'div.k7n_28.n7k_28 span')

    for selector in selectors:
        try:
            element = page.locator(selector)
            if await element.count() > 0:
                text = await element.first.text_content()
                if text:
                    price = ''.join(filter(str.isdigit, text))
                    if price:
                        return price
        except Exception:
            continue

    return 'Цена не найдена'


async def parse_ozon_product(urls):
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )

    chrome_args = [
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions"
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=chrome_args
        )

        context = await browser.new_context(
            user_agent=user_agent,
            locale="ru-RU",
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True
        )

        await context.add_init_script(stealth_js)

        page = await context.new_page()

        for url in urls:
            await page.goto(url, timeout=10000)

            title = await page.locator('h1').text_content()
            price = await extract_price(page)

            print(f'Название товара: {title.strip()}')
            print(f'Цена: {price}')

        await browser.close()


if __name__ == '__main__':
    url1 = 'https://www.ozon.ru/product/kofe-v-zernah-tasty-coffee-braziliya-serrado-1-kg-643726547/'
    url2 = 'https://www.ozon.ru/product/toughbuilt-tb-h4-30-hb-skladnoy-instrumentalnyy-nozh-s-orlinym-klyuvom-1701173779/'
    url3 = 'https://www.ozon.ru/product/solvie-proteinovoe-pechene-bez-sahara-assorti-8sht-8-vkusov-35-belka-1841219486/'
    url4 = 'https://www.ozon.ru/product/bobber-chehol-dlya-termosa-flask-770-ml-termochehol-1608374723/'
    url5 = 'https://www.ozon.ru/product/milwaukee-48-22-2903-14-v-1-otvertka-s-hrapovym-mehanizmom-vysokiy-krutyashchiy-moment-1906337729/'
    asyncio.run(parse_ozon_product((url1, url2, url3, url4, url5, url1, url2, url3, url4, url5, url1, url2, url3, url4, url5, url1, url2, url3, url4, url5)))
