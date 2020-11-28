import time

import pytest
import allure

from helper.logger import logger
from page.exchange import ExchangePage
from page.trade import TradePage


@pytest.mark.usefixtures('client')
class TestTradePage:
    url = 'https://crypto.com/exchange'
    pair_x = 'CRO'
    pair_y = 'USDC'
    trade_url = 'https://crypto.com/exchange/trade/spot/CRO_USDC'
    candle_color = 'blue'

    def test_modify_candle_color(self, client):
        self.driver = client
        page = ExchangePage(self.driver)
        with allure.step('Open Exchange page'):
            page.open(self.url)

        with allure.step('Click tag CRO Markets'):
            page.select_tag_cro_markets()
            page.accept_cookies()

        with allure.step(f'Click Pair {self.pair_x}/{self.pair_y} Trade button'):
            page.click_trade_btn(self.pair_x, self.pair_y)
            time.sleep(3)
            assert page.get_url() == self.trade_url

        page = TradePage(self.driver)
        with allure.step('Click header properties icon'):
            page.switch_to_trading_view()
            page.click_canvas_settings()
        time.sleep(2)

        with allure.step('Select Style tag in pop up window'):
            page.select_canvas_settings_style_tag()

        with allure.step('Click canvas candle color one'):
            page.click_canvas_candle_color_one()
        time.sleep(2)

        with allure.step(f'Select color {self.candle_color}'):
            page.select_candle_color(self.candle_color)
        time.sleep(2)

        with allure.step('Click OK button'):
            page.click_canvas_settings_ok()

        time.sleep(5)

    def test_failure_screenshot_showcase(self, client):
        self.driver = client
        page = ExchangePage(self.driver)
        with allure.step('Open Exchange page'):
            page.open(self.url)

        with allure.step('Click tag CRO Markets'):
            page.select_tag_cro_markets()
            page.accept_cookies()

        with allure.step(f'Click Pair {self.pair_x}/{self.pair_y} Trade button'):
            page.click_trade_btn(self.pair_x, self.pair_y)
            time.sleep(3)
            assert page.get_url() == self.url
