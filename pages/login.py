from selenium.webdriver.chrome.webdriver import WebDriver

from data.data import Datae
from pages.base import BasePage
import pages.locators as locators


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    def login(self, user_name: str = Datae.user_name):
        """
        Performs a login as the given user.

        :param user_name: The username to log in as. Defaults to Harry Potter.
        :type user_name: str
        """
        self.click_to_element(locators.LoginPage.customer_login_button)
        self.select_from_dropdown_by_visible_text(
            locators.LoginPage.customer_dropdown_select, user_name
        )
        self.click_to_element(
            locators.LoginPage.customer_login_button_after_dropdown_selected
        )

    def should_be_user_name(self, user_name):
        """
        Checks that the user name is as expected.

        :param user_name: The user name to check for.
        :return: True if the user name matches the given one, False otherwise.
        """
        return self.get_text(locators.AccountPage.welcome_name) == user_name
