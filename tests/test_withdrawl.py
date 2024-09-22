import time
import allure
from data import functions
from data.urls import Urls
from pages.account import AccountPage


@allure.title(
    "Выполнить списание со счета (Withdrawl) на сумму равную N-е число Фибоначчи, где N - это текущий день месяца + 1"
)
def test_withdrawl(driver):

    # Preconditions
    amount = functions.get_fibonacci_from_current_day_number()
    withdrawl_successfull_message = "Transaction successful"

    page = AccountPage(driver, Urls.LOGIN)
    page.open()
    page.login()
    page.deposit(amount)
    balance_before = page.get_current_balance()

    # Test
    page.withdraw(amount)

    assert page.should_be_transaction_info_message(
        withdrawl_successfull_message
    ), "Successful transaction message differs or absent"

    assert page.should_be_correct_balance(
        balance_before, amount
    ), f"Current balance is <{page.get_current_balance()}>, but it should be <{int(balance_before) - amount}>"
