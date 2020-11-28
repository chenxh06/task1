import time

from element.exchange_page import exchange_page
from helper.web_client import WebClient


class ExchangePage(WebClient):
    def __init__(self, driver=None):
        super(ExchangePage, self).__init__(driver)

    def accept_cookies(self):
        if self.find(exchange_page['accept_cookies_btn'], timeout=5):
            cookies_btn = self.get(exchange_page['accept_cookies_btn'])
            self.execute_js('arguments[0].click();', cookies_btn)

    def select_tag_cro_markets(self):
        self.click(exchange_page['tag_cro_markets'])

    def click_trade_btn(self, x, y):
        btn = self.get(exchange_page['trade_btn'](x, y))
        btn.location_once_scrolled_into_view
        time.sleep(1)
        btn.click()
