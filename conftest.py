import pytest
from selenium import webdriver


@pytest.fixture
def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless=new")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    # print("\nBrowser has been closed...")