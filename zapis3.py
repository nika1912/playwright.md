# ФИО: Адаменко Вероника Алексеевна
# Дата: 2026-11-11
# Время:21:32
# Описание: В этом файле я использую маркеры из справочника Pytest.
# Что изменено (20-30%):
# 1. Использован маркер @pytest.mark.skip_browser("firefox") из справочника для теста навигации.
# 2. Добавлен тест test_navigation_to_api, проверяющий переход на страницу API.
# Зачем: Это демонстрирует умение управлять запуском тестов в разных браузерах.

import re
import pytest
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

# ИЗМЕНЕНИЕ: Используем маркер из справочника, чтобы этот тест не запускался в Firefox
@pytest.mark.skip_browser("firefox")
def test_navigation_to_api(page: Page):
    page.goto("https://playwright.dev/")
    
    # Кликаем по ссылке "API" в верхнем меню
    page.get_by_role("link", name="API").first.click()
    
    # Проверяем, что мы перешли на страницу API
    expect(page).to_have_title(re.compile("API"))

# ИЗМЕНЕНИЕ: Новый тест для проверки переключения темы
def test_dark_mode(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Toggle dark mode").click()
    expect(page.get_by_role("button", name="Toggle dark mode")).to_be_visible()