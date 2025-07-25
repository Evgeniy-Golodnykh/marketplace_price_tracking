START = 'start'
START_DESC = 'Начать работу'
START_MESSAGE = (
    'Привет, {name}!\nВыберите дальнейшее действие и списка ниже:'
)

MENU = 'menu'
MENU_DESC = 'Главное меню'
MENU_MESSAGE = 'Главное меню.\nВыберите дальнейшее действие из списка ниже:'

FAVORITE = 'favorite'
FAVORITE_DESC = 'Избранные товары'
FAVORITE_MESSAGE = 'Ваши избранные товары:\n'
FAVORITE_NOT_EXISTS_MESSAGE = 'Избранные товары отсуствуют.'

INFO = 'info'
INFO_DESC = 'О боте'
INFO_MESSAGE = (
    'Бот помогает отслеживать изменение цен товаров на маркетплейсах Ozon, '
    'Яндекс.Маркет и Wildberries.\nНажмите кнопку <b>«Добавить товар»</b>, '
    'затем введите ссылку на интересующую Вас позицию, укажите желаемую '
    'стоимость и срок отслеживания. Как только стоимость товара достигнет '
    'указанной цены, Вам будет направлено уведомление.\nНажмите кнопку '
    '<b>«Избранные товары»</b>, чтобы увидеть все товары, за изменением цен '
    'которых Вы следите в данный момент.'
)

ADD_ITEM_MESSAGE = 'Добавить товар'
ITEM_ADDED_MESSAGE = (
    '<b>{name}</b> успешно добавлен в список отслеживаемых. Текущая цена '
    'товара - <b>{price} ₽.</b>\nКак только стоимость товара достигнет '
    'желаемой цены, Вам будет направлено уведомление.'
)
GET_LINK_MESSAGE = 'Отправьте ссылку на товар:'
GET_PRICE_MESSAGE = 'Введите желаемую цену на товар:'
GET_DURATION_MESSAGE = (
    'Пожалуйста, выберите срок отслеживания товара из списка ниже:'
)

ERROR_LINK_MESSAGE = (
    'Пожалуйста, введите корректную ссылку на товар из '
    'Ozon, Яндекс.Маркет или Wildberries.'
)
ERROR_EXISTS_LINK_MESSAGE = (
    'Товар с указанной ссылкой уже добавлен в список отслеживаемых.\n'
    'Укажите ссылку на другой товар или маркетплейс.'
)
ERROR_PRICE_MESSAGE = 'Пожалуйста, введите целое положительное число'
ERROR_ADD_ITEM_MESSAGE = (
    'Не получилось добавить данный товар, скорее всего маркетплейс блокирует '
    'данное приложение при поисковом запросе.'
)
