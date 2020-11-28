import os
from pathlib import Path

from selenium import webdriver


class Config:
    # path
    PROJECT_DIR = Path(os.path.dirname(__file__))
    DRIVER_DIR = str(PROJECT_DIR / Path('webdriver'))
    LOG_DIR = str(PROJECT_DIR / Path('log'))
    REPORT_DIR = str(PROJECT_DIR / Path('allure-report/'))
    RESULT_DIR = str(PROJECT_DIR / Path('allure-results'))

    # driver
    BROWSER = {
        'chrome': webdriver.Chrome
    }
    DRIVER = {
        'chrome': str(DRIVER_DIR / Path('chromedriver.exe'))
    }

    # logger
    LOGGER = 'dev'
    DEFAULT_LOG_LEVEL = 'INFO'
