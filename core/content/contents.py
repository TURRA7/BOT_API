"""
Модуль содержит контент для бота.

Args:
    messages: Основные текстовые сообщения бота.
    emoticons: Представления кнопок навигации.
    url: URL адреса для запросов в основное приложение.
    instruction: Инструкции по боту для пользователя.
"""
messages = {
    1: "Бот запущен!",
    2: "Бот остановлен!",
    3: "Доступ запрещён!",
    4: "Мониторинг товаров МВИДЕО, выберите пункт меню:",
    5: "Укажите ссылку на API МВИДЕО с основной инфо о товаре:",
    6: "Укажите ссылку на API МВИДЕО с инфо о цене товара:",
    7: "Укажите id товара в базе:",
}
emoticons = {
    1: "📜ИНСТРУКЦИЯ📜",
    2: "✅ДОБАВИТЬ ТОВАР✅",
    3: "🔥УДАЛИТЬ ТОВАР🔥",
    4: "📊ТОВАРЫ НА МОНИТОРИНГЕ📊",
    5: "📒ИСТОРИЯ ЦЕН ТОВАРА📒",
}
url = {
    "add": "http://127.0.0.1:8000/parsing/add_product",
    "delete": "http://127.0.0.1:8000/parsing/delete_product",
    "get_list": "http://127.0.0.1:8000/parsing/get_list_monitoring",
    "get_history": "http://127.0.0.1:8000/parsing/get_history_price_item",
}
instruction = {
    1: ("* Для добавления товара:\n"
        "    1. Перейдите в браузер и откройте товар магазина МВИДЕО.\n"
        "    2. Откройте инструменты разработчика(клавиша F12).\n"
        "    3. Перейдите во вкладку Network и выберите фильтр Fetch/XHR.\n"
        "    4. Обновите страницу, далее во вкладке запросов, найдите 2 запроса\n"
        "- Один из них будет вида: product-details?multioffer=true&productId=...,\n"
        "- Другой будет вида: products/prices?addBonusRubles=true&is...\n"
        "    5. Во вкладке Headers запроса, скопируйте URL адреса."
        "    6. После перейдите в телеграм бот, нажмите кнопку 'ДОБАВИТЬ ТОВАР',\n"
        "- А далее по очерёдно и отдельно отправьте ссылки боту, согласно подсказкам.\n"
        " * ВАЖНО: запрос типа: \n"
        "- product-details... отправляется первым,\n"
        "- Запрос типа products/prices... отправляется вторым!\n"
        "* Для удаления товара:\n"
        "    1. Нажмите на кнопку 'УДАЛИТЬ ТОВАР'\n"
        "    2. Введите id товара из базы данных, отправьте ответ\n"
        "* Узнать какие товары сейчас на мониторинге в базе,\n"
        "можно нажав на кнопку 'ТОВАРЫ НА МОНИТОРИНГЕ' в меню\n"
        " * Для получения истории цен на товар,\n"
        "    1. Нажмите на кнопку 'УДАЛИТЬ ТОВАР'\n"
        "    2. Введите id товара из базы данных, отправьте ответ\n"),
}