import allure
from data import functions


@allure.feature("Операции со счетом")
@allure.story("Зачисление средств")
@allure.title(
    "Выполнить пополнение счета (Deposit) на сумму равную N-е число Фибоначчи, где N - это текущий день месяца + 1"
)
@allure.severity(allure.severity_level.BLOCKER)
def test_deposit(setup_account_page_to_deposit):
    """
    Test depositing a sum equal to the Nth Fibonacci number, where N is the current day of the month + 1.

    Preconditions:
    - The amount to be deposited is a Fibonacci number.
    - The deposit transaction is successful.

    Steps:
    1. Get amount to be deposited.
    3. Deposit the amount.
    4. Verify that the transaction is successful.
    5. Verify that the balance is increased by the deposited amount.
    """

    with allure.step("Подготавливаем предусловия теста"):
        page, balance_before = setup_account_page_to_deposit
        amount_to_be_deposited = functions.get_fibonacci_from_current_day_number()
        deposit_successfull_message = "Deposit Successful"

    with allure.step("Пополняем счет"):
        page.deposit(amount_to_be_deposited)

    with allure.step("Проверяем сообщение об успешности транзации"):
        assert page.should_be_transaction_info_message(
            deposit_successfull_message
        ), "Successful transaction message differs or absent"

    with allure.step(
        "Проверяем, что баланс после списания соответствует сумме баланса до списания и суммы пополнения"
    ):
        assert page.should_be_correct_balance_after_deposit(
            balance_before, amount_to_be_deposited
        ), f"Current balance is <{page.get_current_balance()}>, but it should be <{int(balance_before) + amount_to_be_deposited}>"
