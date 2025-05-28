avito = {
    'price_selectors': [
        'span[itemprop="price"]',
        'span.m1q_28.qm1_28.q5m_28',
    ],
    'title_selectors': [
        'h1[itemprop="name"]',
        'h2[class="firewall-title"]',
    ]
}

ozon = {
    'price_selectors': [
        'span.mp7_28.m5p_28',
        'span.m1q_28.qm1_28.q5m_28',
    ],
    'title_selectors': [
        'h1',
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
