import allure
from data import functions
from data.urls import Urls
from pages.account import AccountPage


@allure.title(
    "Выполнить пополнение счета (Deposit) на сумму равную N-е число Фибоначчи, где N - это текущий день месяца + 1"
)
def test_deposit(driver):

    # Preconditions
    amount_to_be_deposited = functions.get_fibonacci_from_current_day_number()
    deposit_successfull_message = "Deposit Successful"

    page = AccountPage(driver, Urls.LOGIN)
    page.open()
    page.login()

    # Test
    page.deposit(amount_to_be_deposited)

    assert page.should_be_transaction_info_message(deposit_successfull_message)
    assert page.should_be_same_amount_on_balance_equal_to_deposited(
        amount_to_be_deposited
    )
