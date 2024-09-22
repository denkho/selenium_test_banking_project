import allure
from data import functions
from data.urls import Urls
from pages.account import AccountPage


@allure.title(
    "Выполнить пополнение счета (Deposit) на сумму равную N-е число Фибоначчи, где N - это текущий день месяца + 1"
)
def test_deposit(driver):
    """
    Test depositing a sum equal to the Nth Fibonacci number, where N is the current day of the month + 1.

    Preconditions:
    - The amount to be deposited is a Fibonacci number.
    - The deposit transaction is successful.

    Steps:
    1. Open the website.
    2. Log in.
    3. Deposit the amount.
    4. Verify that the transaction is successful.
    5. Verify that the balance is increased by the deposited amount.
    """

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
