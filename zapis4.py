# ФИО: Адаменко Вероника Алексеевна
# Дата: 2026-11-12
# Время: 10:01
# Описание: В этом файле я использую расширенные настройки контекста и отчетов из справочника Pytest.
# Что изменено (20-30%):
# 1. Добавлена фикстура browser_context_args, которая задает кастомный размер экрана (1920x1080).
# 2. Добавлен тест test_custom_viewport, проверяющий, что размер экрана применился.
# 3. В тесте test_failure_screenshot показано, как делать скриншот при падении (через параметры командной строки).
# Зачем: Это демонстрирует умение настраивать окружение (кастомный экран) и использовать отладочные инструменты Playwright.

import re
import pytest
from playwright.sync_api import Page, expect

# ИЗМЕНЕНИЕ: Настройка кастомного размера экрана через фикстуру
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

# ИЗМЕНЕНИЕ: Новый тест, который проверяет, что размер экрана действительно 1920x1080
def test_custom_viewport(page: Page):
    page.goto("https://playwright.dev/")
    
    viewport_size = page.evaluate("() => ({ width: window.innerWidth, height: window.innerHeight })")
    assert viewport_size["width"] == 1920
    assert viewport_size["height"] == 1080

# ИЗМЕНЕНИЕ: Пример теста, который может упасть (чтобы проверить скриншот при падении)
# Если запустить pytest с флагом --screenshot on, при падении этого теста сохранится скриншот.
def test_failure_screenshot(page: Page):
    page.goto("https://playwright.dev/")
    # Специально проверяем то, чего нет, чтобы тест упал (для демонстрации)
    expect(page).to_have_title(re.compile("NonExistentTitle"))