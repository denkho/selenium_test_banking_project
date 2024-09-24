import allure


@allure.title("Проверка наличия транзакций депозита и снятия суммы")
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

    page, transactions = setup_account_page_to_check_transactions_table

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

    for i in range(len(transactions)):
        assert (
            transactions[i] == transactions_table[i + 1]
        ), f"Transaction done is <{transactions[i]}>, but in the table it is <{transactions_table[i + 1]}>"
