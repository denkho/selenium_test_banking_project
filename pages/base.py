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
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_to_element(self, locator):
        self.element_is_visible(locator).click()

    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def fill_in_input_field(self, locator, data):
        self.element_is_visible(locator).send_keys(data)

    def select_from_dropdown_by_visible_text(self, locator, text):
        select = Select(self.element_is_visible(locator))
        select.select_by_visible_text(text)
