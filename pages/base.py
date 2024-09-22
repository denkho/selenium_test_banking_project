from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    timeout = 10

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        """
        Opens the page by navigating to the URL given during initialization.
        """
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=timeout):
        """
        Waits until an element is visible and clickable.

        :param locator: Locator of the element to wait for.
        :param timeout: Timeout in seconds. Defaults to the class's timeout.
        :return: The element that matched the given locator.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def elements_are_visible(self, locator, timeout=timeout):
        """
        Waits until elements are visible.

        :param locator: Locator of the elements to wait for.
        :param timeout: Timeout in seconds. Defaults to the class's timeout.
        :return: List of the elements that matched the given locator.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_to_element(self, locator):
        """
        Click an element.

        :param locator: Locator of the element to click.
        """
        
        self.element_is_visible(locator).click()

    def get_text(self, locator):
        """
        Get the text from an element.

        :param locator: Locator of the element.
        :return: The text of the element.
        """
        return self.element_is_visible(locator).text

    def fill_in_input_field(self, locator, data):
        """
        Fill in an input field with given data.

        :param locator: Locator of the input element.
        :param data: Data to fill in the input field.
        """
        self.element_is_visible(locator).send_keys(data)

    def select_from_dropdown_by_visible_text(self, locator, text):
        """
        Select an option in a dropdown by its visible text.

        :param locator: Locator of the dropdown element.
        :param text: Visible text of the option to select.
        """
        select = Select(self.element_is_visible(locator))
        select.select_by_visible_text(text)
