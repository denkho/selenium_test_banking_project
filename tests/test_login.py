import allure
from data.data import Datae
from data.urls import Urls
from pages.login import LoginPage as LP


@allure.feature("Авторизация")
@allure.story("Авторизация с валидными данными")
@allure.title("Авторизоваться пользователем «Harry Potter»")
@allure.severity(allure.severity_level.BLOCKER)
def test_login(driver):
    """
    This test logs in as Harry Potter and checks that the user name is present
    and matches the given user name.
    """
    with allure.step("Открываем страницу и авторизуемся"):
        page = LP(driver, Urls.LOGIN)
        page.open()
        page.login(Datae.user_name)

    with allure.step(
        "Проверяем, что пользователь, которым авторизовались соответствует тому, который в системе"
    ):
        assert page.should_be_user_name(
            Datae.user_name
        ), f"There should be user name <{Datae.user_name}>, but it is absent or differs."
