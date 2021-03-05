import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # сохраняем переданный в консоли параметр в переменную
    language_pref = request.config.getoption("language")
    if isinstance(language_pref, type(None)):
        raise pytest.UsageError("--language should be a ISO language code")
    else:
        # добавляем заголовок запроса "язык пользователя"
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_pref})
        # запускаем хром с указанным языком
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    # закрываем браузер после выполнения теста
    yield browser
    browser.quit()
