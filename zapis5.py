# ФИО: Адаменко Вероника Алексеевна
# Дата: 2026-11-13
# Время: 13:20
# Описание: В этом файле я использую расширенные настройки контекста и отчетов из справочника Pytest.
# Что изменено (20-30%):
# 1. В фикстуре browser_context_args изменен размер экрана на 1280x720 и добавлен device_scale_factor: 2.
# 2. В тесте test_custom_viewport добавлена проверка плотности пикселей (window.devicePixelRatio).
# 3. В тесте test_failure_screenshot изменен ожидаемый заголовок для наглядной демонстрации падения.
# Зачем: Это демонстрирует умение настраивать окружение под конкретные устройства (ноутбук с Retina), 
# а также показывает более глубокую проверку контекста браузера.

import re
import pytest
from playwright.sync_api import Page, expect

# ИЗМЕНЕНИЕ: Настройка кастомного размера экрана и плотности пикселей
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,   # изменено с 1920 на 1280 (эмуляция ноутбука)
            "height": 720,   # изменено с 1080 на 720
        },
        "device_scale_factor": 2  # добавлено: эмуляция Retina-экрана
    }

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

# ИЗМЕНЕНИЕ: Тест проверяет не только размер, но и масштаб пикселей
def test_custom_viewport(page: Page):
    page.goto("https://playwright.dev/")
    
    viewport_data = page.evaluate("() => ({ width: window.innerWidth, height: window.innerHeight, ratio: window.devicePixelRatio })")
    
    assert viewport_data["width"] == 1280
    assert viewport_data["height"] == 720
    assert viewport_data["ratio"] == 2  # добавлено: проверка device_scale_factor

# ИЗМЕНЕНИЕ: Изменен текст ожидания, чтобы тест гарантированно упал для демонстрации
def test_failure_screenshot(page: Page):
    page.goto("https://playwright.dev/")
    # Специально ищем заголовок, которого нет, чтобы продемонстрировать падение
    expect(page).to_have_title(re.compile("ThisTitleDoesNotExist"))