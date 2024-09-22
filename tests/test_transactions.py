import allure
import time

from data import functions
from data.urls import Urls
from pages.account import AccountPage


@allure.title("Проверка наличия обеих транзакций")
def test_transactions(driver):
    """
    This test checks that both deposit and withdraw transactions are present in the transactions table.

    Preconditions:
    - The deposit and withdraw transactions have been performed.

    Steps:
    1. Open the transactions table page.
    2. Save the transactions table page to a CSV file.
    3. Attach the CSV file to the report.
    4. Check that the transactions table contains two transactions.

    Expected result:
    The transactions table contains two transactions.
    """
    # Preconditions
    amount = functions.get_fibonacci_from_current_day_number()

    page = AccountPage(driver, Urls.LOGIN)
    page.open()
    page.login()
    page.deposit(amount)

    page.withdraw(amount)
    time.sleep(5)

    # Test
    page.open_transactions_table()

    transactions_table = page.get_data_from_transactions_table()
    page.get_transactions_table_csv_file()
    allure.attach.file(
        "data/transactions.csv",
        name="Transactions",
        attachment_type=allure.attachment_type.CSV,
    )

    assert (
        len(transactions_table) == 3
    ), "Transactions has not been written in the table or some other problem"
