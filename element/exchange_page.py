from selenium.webdriver.common.by import By

exchange_page = {
    'accept_cookies_btn': (By.CSS_SELECTOR, 'button.optanon-allow-all.accept-cookies-button'),
    'tag_cro_markets': (By.XPATH, '//div[text()="CRO Markets"]'),
    'trade_btn': lambda x, y: (By.XPATH, '//span[@class="source" and text()="{0}"]/following-sibling::span[@class="target" and text()="/{1}"]/../../../div[7]'.format(x, y)),
}
