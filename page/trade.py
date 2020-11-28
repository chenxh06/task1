from element.trade_page import trade_page, canvas_settings
from helper.web_client import WebClient


class TradePage(WebClient):
    def __init__(self, driver=None):
        super(TradePage, self).__init__(driver)

    def select_tag_market(self):
        self.click(trade_page['tag_market'])

    def input_buy_amount(self, amount: str):
        input_field = self.get_all(trade_page['textfield_buy_amount'])[1]
        input_field.send_keys(amount)

    def switch_to_trading_view(self):
        self.driver.switch_to.frame(self.get(canvas_settings['iframe']))

    def click_canvas_settings(self):
        self.click(trade_page['canvas_settings'])

    def select_canvas_settings_style_tag(self):
        self.click(canvas_settings['tag_style'])

    def click_canvas_candle_color_one(self):
        self.click(canvas_settings['candle_color_one'])

    def select_candle_color(self, color: str):
        self.click(canvas_settings[f'color_{color}'])

    def click_canvas_settings_ok(self):
        self.click(canvas_settings['ok_btn'])
