import platform

import allure
import pytest

from config import Config

platform_os = platform.system().lower()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Browser name: currently available [chrome]'
    )


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='function', autouse=True)
def client(request, browser):
    driver = Config.BROWSER[browser](executable_path=Config.DRIVER[browser]) if platform_os.startswith('windows') else \
        Config.BROWSER[browser]()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_exception_interact(node, call, report):
    try:
        driver = node.instance.driver
        allure.attach(driver.get_screenshot_as_png(), 'Fail screenshot', allure.attachment_type.PNG)
    except AttributeError:
        pass
