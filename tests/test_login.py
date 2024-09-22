import allure
from data.data import Datae
from data.urls import Urls
from pages.login import LoginPage as LP

@allure.title("Авторизоваться пользователем «Harry Potter»")
def test_login(driver):
    """
    This test logs in as Harry Potter and checks that the user name is present
    and matches the given user name.
    """
    page = LP(driver, Urls.LOGIN)
    page.open()
    page.login(Datae.user_name)

    assert page.should_be_user_name(
        Datae.user_name
    ), f"There should be user name <{Datae.user_name}>, but it is absent or differs."
