import allure
from data import functions


@allure.title(
    "Выполнить списание со счета (Withdrawl) на сумму равную N-е число Фибоначчи, где N - это текущий день месяца + 1"
)
def test_withdrawl(setup_account_page_to_withdraw):
    """
    Test withdrawl transaction.

    Preconditions:
    - The amount to be withdrawn is a Fibonacci number.
    - The withdrawl transaction is successful.

    Steps:
    1. Open the website.
    2. Log in.
    3. Deposit the amount.
    4. Withdraw the amount.
    5. Verify that the transaction is successful.
    6. Verify that the balance is decreased by the withdrawn amount.
    """

    amount = functions.get_fibonacci_from_current_day_number()
    withdrawl_successfull_message = "Transaction successful"

    page, balance_before = setup_account_page_to_withdraw

    page.withdraw(amount)

    assert page.should_be_transaction_info_message(
        withdrawl_successfull_message
    ), "Successful transaction message differs or absent"

    assert page.should_be_correct_balance_after_withdrawl(
        balance_before, amount
    ), f"Current balance is <{page.get_current_balance()}>, but it should be <{int(balance_before) - amount}>"
