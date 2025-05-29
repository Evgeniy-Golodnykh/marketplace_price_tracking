ozon = {
    'price_selectors': [
        'span.mp7_28.m5p_28',
        'span.m1q_28.qm1_28.q5m_28',
    ],
    'title_selectors': [
        'h1',
    ]
}

wildberries = {
    'price_selectors': [
        'span[class="price-block__wallet-price red-price"]',
        'span[class="price-block__wallet-price"]',
        'ins[class="price-block__final-price"]',
    ],
    'title_selectors': [
        'h1[class="product-page__title"]',
    ]
}

yandex = {
    'price_selectors': [
        'span[data-auto="snippet-price-current"]',
        'span[data-auto="price-block"]',
    ],
    'title_selectors': [
        'h1[data-auto="productCardTitle"]',
    ]
}
