browser_config = {
    'user_agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/123.0.0.0 Safari/537.36'
    ),
    'chrome_args': (
        '--no-sandbox',
        '--disable-gpu',
        '--disable-dev-shm-usage',
        '--disable-extensions'
    ),
    'viewport': {'width': 1280, 'height': 800},
    'locale': 'ru-RU',
    'price_selectors': [
        'span[class="om7_27 o5m_27"]',
        'span.mp7_28.m5p_28',
        'span.m1q_28.qm1_28.q5m_28',
        'span[data-auto="snippet-price-current"]',
        'span[data-auto="price-block"]',
        'span[class="price-block__wallet-price red-price"]',
        'span[class="price-block__wallet-price"]',
        'ins[class="price-block__final-price"]',
    ],
    'title_selectors': [
        'h1',
        'h1[data-auto="productCardTitle"]',
        'h1[class="product-page__title"]',
    ]
}

stealth_js = '''
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
'''
