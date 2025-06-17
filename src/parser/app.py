import asyncio
from parser.core import run_parser

url1 = 'https://www.ozon.ru/product/syr-slivochnyy-45-200-g-natura-143412218/'
url2 = 'https://www.ozon.ru/product/noski-allure-774445283/'
url3 = 'https://www.ozon.ru/product/shchetka-dlya-velosipeda-1570457818/'
url4 = 'https://www.ozon.ru/product/bolt-1659053101/'
url5 = 'https://www.ozon.ru/product/toughbuilt-molotok-stolyarnyy-1879680201/'
urls = [url1, url2, url3, url4, url5, url1, url2, url3, url4, url5, url1, url2]
print(asyncio.run(run_parser(url1)))
print(asyncio.run(run_parser(url5)))

url7 = 'https://market.yandex.ru/product--is-7143-wh/61072168'
url8 = 'https://market.yandex.ru/product--vitamin-d3/1775010076'
url9 = 'https://market.yandex.ru/product--3615-1016/1772866751'
urls = [url7, url8, url9, url7, url8, url9, url7, url8, url9, url7, url8, url9]
print(asyncio.run(run_parser(url7)))
print(asyncio.run(run_parser(url8)))

url7 = 'https://www.wildberries.ru/catalog/138834549/detail.aspx'
url8 = 'https://www.wildberries.ru/catalog/303328540/detail.aspx'
url9 = 'https://www.wildberries.ru/catalog/14126423/detail.aspx'
urls = [url7, url8, url9, url7, url8, url9, url7, url8, url9, url7, url8, url9]
print(asyncio.run(run_parser(url8)))
print(asyncio.run(run_parser(url9)))
