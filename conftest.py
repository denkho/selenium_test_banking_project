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

    grid_url = "http://localhost:4444/wd/hub"

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=chrome_options
    )
    # driver = webdriver.Chrome(options=chrome_options) # для локального запуска не в GRID

    yield driver
    driver.quit()
    # print("\nBrowser has been closed...")