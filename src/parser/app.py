import asyncio
from parser.configs import browser_config, ozon_selectors, stealth_js
from parser.core import run_parser

browser_config.update(ozon_selectors)
url1 = 'https://www.ozon.ru/product/syr-slivochnyy-45-200-g-natura-143412218/'
url2 = 'https://www.ozon.ru/product/noski-allure-774445283/'
url3 = 'https://www.ozon.ru/product/shchetka-dlya-velosipeda-1570457818/'
url4 = 'https://www.ozon.ru/product/bolt-1659053101/'
url5 = 'https://www.ozon.ru/product/toughbuilt-molotok-stolyarnyy-1879680201/'

urls = [
    url1, url2, url3, url4, url5, url1, url2, url3, url4, url5, url1, url2,
    url3, url4, url5, url1, url2, url3, url4, url5, url1, url2, url3, url4,
]

asyncio.run(run_parser(urls, browser_config, stealth_js))
