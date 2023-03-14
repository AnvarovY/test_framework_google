import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.headless = False
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
