import allure


@allure.feature("Операции со счетом")
@allure.story("Проверка списка транзакций")
@allure.title("Проверка наличия транзакций депозита и снятия суммы")
@allure.severity(allure.severity_level.CRITICAL)
def test_transactions(setup_account_page_to_check_transactions_table):
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
    with allure.step("Подготавливаем предусловия теста"):
        page, transactions = setup_account_page_to_check_transactions_table

    with allure.step("Открываем страницу с транзакциями"):
        page.open_transactions_table()

    with allure.step("Собираем данные из таблицы для последующей проверки"):
        transactions_table = page.get_data_from_transactions_table()

    with allure.step("Сохраняем данные о транзакциях в CSV файл"):
        page.get_transactions_table_csv_file(transactions_table)
        allure.attach.file(
            "data/transactions.csv",
            name="Transactions",
            attachment_type=allure.attachment_type.CSV,
        )

    with allure.step(
        "Проверяем, что количество транзакций в таблице соответсвует количеству совершенных"
    ):
        assert (
            len(transactions_table) == 3
        ), "Transactions has not been written in the table or some other problem"

    with allure.step(
        "Проверяем, что транзации в таблице соответсвуют совершенным транзакциям"
    ):
        for i in range(len(transactions)):
            assert (
                transactions[i] == transactions_table[i + 1]
            ), f"Transaction done is <{transactions[i]}>, but in the table it is <{transactions_table[i + 1]}>"
