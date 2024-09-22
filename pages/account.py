import csv

from datetime import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages import locators
from pages.login import LoginPage


class AccountPage(LoginPage):

    def __init__(self, driver: WebDriver, url):
        super().__init__(driver, url)

    def deposit(self, amount):
        """
        Perform a deposit of the given amount.

        :param amount: The amount to deposit.
        """
        self.click_to_element(locators.AccountPage.deposit_form_button)
        self.fill_in_input_field(locators.AccountPage.input_amount_deposit_field, amount)
        self.click_to_element(locators.AccountPage.deposit_action_button)

    def withdraw(self, amount):
        """
        Perform a withdraw of the given amount.

        :param amount: The amount to withdraw.
        """
        self.click_to_element(locators.AccountPage.withdrawl_form_button)
        self.fill_in_input_field(locators.AccountPage.input_amount_withdraw_field, amount)
        self.click_to_element(locators.AccountPage.withdrawl_action_button)

    def open_transactions_table(self):
        """
        Opens the transactions table page.
        """
        self.click_to_element(locators.AccountPage.transactions_form_button)

    def should_be_transaction_info_message(self, message):
        """
        Checks that the transaction message is as expected.

        :param message: The message to check for.
        """
        return self.get_text(locators.AccountPage.message_about_transaction) == message

    def get_current_balance(self):
        """
        Gets the current balance displayed on the page.

        :return: The current balance as a string.
        """
        return self.get_text(locators.AccountPage.balance_amount)

    def should_be_same_amount_on_balance_equal_to_deposited(self, amount):
        """
        Checks that the current balance is the same as the given amount.

        :param amount: The amount to check against.
        """
        return self.get_text(locators.AccountPage.balance_amount) == str(amount)

    def should_be_correct_balance(self, balance_before: str, amount: int):
        """
        Checks that the current balance is the same as the given balance before minus the given amount.

        :param balance_before: The balance before the transaction.
        :param amount: The amount of the transaction.
        """
        return int(self.get_current_balance()) == int(balance_before) - amount
    

    def get_data_from_transactions_table(self):
        """
        Gets the data from the transactions table page.

        :return: A 2D list of the data from the table.
        """
        table = self.element_is_visible(locators.AccountPage.transactions_table)
        transactions = []
        for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
            transactions.append([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])

        for i in range(1, len(transactions)):
            dtm = datetime.strptime(transactions[i][0], '%b %d, %Y %I:%M:%S %p').strftime('%d %b %Y %H:%M:%S')
            transactions[i][0] = dtm

        return transactions


    def get_transactions_table_csv_file(self):
        """
        Saves the transactions table as a CSV file named 'transactions.csv' in the 'data' folder.
        """
        table = self.get_data_from_transactions_table()
        with open('data/transactions.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(table)
