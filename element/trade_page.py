from selenium.webdriver.common.by import By

trade_page = {
    'tag_market': (By.XPATH, '//div[text()="Market"]'),
    'textfield_buy_amount': (By.CSS_SELECTOR, 'input[id^=buyAmount]'),
    'canvas_settings': (By.CSS_SELECTOR, 'div#header-toolbar-properties')
}

canvas_settings = {
    'iframe': (By.CSS_SELECTOR, 'iframe[id^=tradingview]'),
    'tag_style': (By.XPATH, '//a[text()="Style"]'),
    'candle_color_one': (By.XPATH, "//td[text()='Candles']/following-sibling::td[1]"),
    'color_blue': (By.CSS_SELECTOR, 'div.tvcolorpicker-swatches-area>table:nth-child(2)>tbody>tr>td:nth-child(7)'),
    'ok_btn': (By.CSS_SELECTOR, 'a._tv-button.ok')
}
