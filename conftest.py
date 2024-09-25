import allure
import pytest
from selenium import webdriver

from data import functions
from data.urls import Urls
from pages.account import AccountPage


@pytest.fixture
def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    return options


@pytest.fixture
def driver(chrome_options):

    grid_url = "http://localhost:4444/wd/hub"

    driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)

    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """
    Fixture to log in as Harry Potter and yield the AccountPage instance after login.

    This fixture is used to log in as Harry Potter and yield the AccountPage instance after login.
    The fixture is used to set up the test environment before each test is run.
    The fixture is used to yield the AccountPage instance after login, so that it can be used in the tests.
    """
    page = AccountPage(driver, Urls.LOGIN)
    page.open()
    page.login()
    yield page


@pytest.fixture
def setup_account_page_to_deposit(login):
    """
    Fixture to set up the test environment before each test is run.

    This fixture is used to set up the test environment before each test is run.
    The fixture is used to yield the AccountPage instance and the balance before depositing, so that it can be used in the tests.

    :return: A tuple of (AccountPage instance, balance before depositing).
    """
    page = login
    balance_before = page.get_current_balance()
    yield page, balance_before


@pytest.fixture
def setup_account_page_to_withdraw(login):
    """
    Fixture to set up the test environment before each test is run.

    This fixture is used to set up the test environment before each test is run.
    The fixture is used to yield the AccountPage instance and the balance before withdrawing, so that it can be used in the tests.

    :return: A tuple of (AccountPage instance, balance before withdrawing).
    """
    page = login
    amount = functions.get_fibonacci_from_current_day_number()
    page.deposit(amount)
    balance_before = page.get_current_balance()
    yield page, balance_before


@pytest.fixture
def setup_account_page_to_check_transactions_table(login):
    """
    Fixture to set up the test environment before each test is run.

    This fixture is used to set up the test environment before each test is run.
    The fixture is used to yield the AccountPage instance and the transactions list, so that it can be used in the tests.

    :return: A tuple of (AccountPage instance, list of transactions).
    """
    page = login
    amount = functions.get_fibonacci_from_current_day_number()

    trasactions = [page.deposit(amount), page.withdraw(amount)]

    yield page, trasactions


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest hook to add screenshot to Allure report if test fails

    When test fails, this hook takes screenshot of the page and attaches it to the test report in Allure
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
