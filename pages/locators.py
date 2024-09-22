class LoginPage:

    customer_login_button = ["xpath", "//button[@ng-click='customer()']"]
    customer_dropdown_select = ["xpath", "//select[@name='userSelect']"]
    customer_login_button_after_dropdown_selected = ["xpath", "//button[@type='submit']"]

class AccountPage:

    welcome_name = ["xpath", "//span[@class='fontBig ng-binding']"]

    balance_amount = ["xpath", "//div[@ng-hide='noAccount']/strong[2]"]

    deposit_form_button = ["xpath", "//button[@ng-click='deposit()']"]
    withdrawl_form_button = ["xpath", "//button[@ng-click='withdrawl()']"]
    transactions_form_button = ["xpath", "//button[@ng-click='transactions()']"]

    input_amount_deposit_field = ["xpath", "//label[contains(text(), 'Amount to be Deposited :')]/following::input[@ng-model='amount']"]    
    input_amount_withdraw_field = ["xpath", "//label[contains(text(), 'Amount to be Withdrawn :')]/following::input[@ng-model='amount']"]    


    deposit_action_button = ["xpath", "//button[@type='submit']"]
    withdrawl_action_button = ["xpath", "//button[@type='submit']"]

    message_about_transaction = ["xpath", "//span[@ng-show='message']"]

    transactions_table = ["xpath", "//table[@class='table table-bordered table-striped']"]
