# ФИО: Адаменко Вероника Алексеевна
# Дата: 2026-11-10
# Время: 13:42
# Описание изменений: Я изменила исходный пример.
# 1. Добавила ожидание загрузки страницы (wait_for_load_state), чтобы тест был стабильнее.
# 2. Заменила print на assert, чтобы код не просто выводил заголовок, а проверяла условие.
# 3. Добавила комментарий к изменению — это составляет примерно 25% изменения исходного кода.
# Зачем: исходный пример только демонстрировал открытие страницы; мой вариант приближен к реальному тесту.

from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.wait_for_load_state()  # добавлено: ожидание полной загрузки
    title = page.title()
    assert "Playwright" in title, f"Ожидалось 'Playwright' в заголовке, получено: {title}"  # изменено: проверка вместо print
    browser.close()