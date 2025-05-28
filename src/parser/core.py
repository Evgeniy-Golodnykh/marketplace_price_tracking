import asyncio

from playwright.async_api import async_playwright


async def extract_price(page, selectors):
    for selector in selectors:
        element = page.locator(selector)
        if await element.count() > 0:
            text = await element.first.text_content()
            if text:
                return int(''.join(filter(str.isdigit, text)))
    return 'Цена отсуствует'


async def extract_title(page, selectors):
    for selector in selectors:
        try:
            title = await page.locator(selector).text_content()
            return title.strip()
        except Exception:
            continue
    return 'Наименование отсуствует'


async def parse_product(page, url, config):
    await page.goto(url, timeout=10000)
    title = await extract_title(page, config['title_selectors'])
    price = await extract_price(page, config['price_selectors'])

    print(f'Название товара: {title}')
    print(f'Цена: {price}')


async def run_parser(urls, config, stealth_js):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=config['chrome_args']
        )

        context = await browser.new_context(
            user_agent=config['user_agent'],
            locale=config['locale'],
            viewport=config['viewport'],
            java_script_enabled=True
        )

        await context.add_init_script(stealth_js)

        pages = [await context.new_page() for _ in urls]
        tasks = [
            parse_product(page, url, config) for page, url in zip(pages, urls)
        ]
        await asyncio.gather(*tasks)

        await browser.close()
