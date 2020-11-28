from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from helper.wrappers import debug_log


class WebClient:
    DEFAULT_GET_TIMEOUT = 60
    DEFAULT_FIND_TIMEOUT = 10

    def __init__(self, driver=None):
        self.driver = driver

    def open(self, url: str):
        """
        webdriver open url
        :param url: website url
        :return:
        """
        self.driver.get(url)

    @debug_log
    def get(self, locator, timeout=DEFAULT_GET_TIMEOUT):
        """
        get element instance
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        :return: element instance
        """
        try:
            return WebDriverWait(self.driver, timeout, 0.5).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f'Element not found: {locator[1]}')

    @debug_log
    def find(self, locator, timeout=DEFAULT_FIND_TIMEOUT):
        """
        find element instance
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        :return: True if element found, else False
        """
        try:
            flag = True
            WebDriverWait(self.driver, timeout, 0.5).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            flag = False
        return flag

    @debug_log
    def get_all(self, locator, timeout=DEFAULT_GET_TIMEOUT) -> list:
        """
        get all matched elements instance
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        :return: list of element instances
        """
        try:
            return WebDriverWait(self.driver, timeout, 0.5).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f'Elements not found: {locator[1]}')

    @debug_log
    def get_clickable(self, locator, timeout=DEFAULT_GET_TIMEOUT):
        """
        get element instance, wait until it is clickable
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        :return: element instance
        """
        try:
            return WebDriverWait(self.driver, timeout, 0.5).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f'Element not found: {locator[1]}')

    @debug_log
    def click(self, locator, timeout=DEFAULT_GET_TIMEOUT):
        """
        click element, when it is clickable
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        :return:
        """
        self.get(locator, timeout).click()

    @debug_log
    def input_text(self, locator, text: str, timeout=DEFAULT_GET_TIMEOUT):
        """
        input text into element
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param text: text needs to input
        :param timeout: search timeout (in seconds)
        :return:
        """
        self.get(locator, timeout).send_keys(text)

    @debug_log
    def input_clear(self, locator, timeout=DEFAULT_GET_TIMEOUT):
        """
        clear text in element
        :param locator: locator tuple. e.g. (By.ID, 'submit')
        :param timeout: search timeout (in seconds)
        """
        self.get(locator, timeout).clear()

    @debug_log
    def execute_js(self, script: str, *args):
        self.driver.execute_script(script, *args)

    def get_url(self):
        """
        :return: current page url
        """
        return self.driver.current_url

    def quit(self):
        if self.driver:
            self.driver.quit()
