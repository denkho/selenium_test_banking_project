import allure
import time

from data import functions
from data.urls import Urls
from pages.account import AccountPage

@allure.title("Проверка наличия обеих транзакций")
def test_transactions(driver):

    amount = functions.get_fibonacci_from_current_day_number()

    page = AccountPage(driver, Urls.LOGIN)
    page.open()
    page.login()
    page.deposit(amount)

    page.withdraw(amount)
    time.sleep(5)
    page.open_transactions_table()

    transactions_table = page.get_data_from_transactions_table()
    page.get_transactions_table_csv_file()
    allure.attach.file("data/transactions.csv", name="Transactions", attachment_type=allure.attachment_type.CSV)

    assert (
        len(transactions_table) == 3
    ), "Transactions has not been written in the table or some other problem"
