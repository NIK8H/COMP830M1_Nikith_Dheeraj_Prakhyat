## ATM Simulator Design Document

### Introduction:
The ATM simulator project is a Python program that simulates the functionality of an ATM. 
Users can perform financial transactions such as checking account balances, making deposits, and withdrawing funds without physically visiting a bank. The project uses object-oriented programming concepts such as encapsulation, inheritance, and polymorphism to model the classes for the ATM, bank account, and transactions.

### Requirements:
The ATM simulator must allow users to create new bank accounts with a unique account number and PIN.
Each bank account must have a starting balance of $0.
Users must be able to check the balance of an account.
Users must be able to deposit funds into an account.
Users must be able to withdraw funds from an account, but only if the account has sufficient funds.
Users must enter a valid PIN to access their account.
Users must be able to change their PIN.
The ATM must display a menu of options to the user and prompt for input.
The ATM must handle incorrect input gracefully and provide appropriate error messages.
The ATM must allow the user to exit the program.
### Classes:
The project consists of three classes: ATM, BankAccount, and Transaction.

#### ATM Class:
The ATM class is responsible for displaying the menu of options to the user and handling user input. The class contains the following methods:

 * display_menu(): Displays the menu of options to the user.
 * create_account(): Prompts the user to enter a new account number and PIN, creates a new BankAccount instance with a starting balance of $0, and adds it to the list of BankAccount instances.
 * check_balance(): Prompts the user to enter their account number and PIN, retrieves the corresponding BankAccount instance from the list, and displays the account balance to the user.
 * deposit(): Prompts the user to enter their account number, PIN, and deposit amount, retrieves the corresponding BankAccount instance from the list, and deposits the amount into the account.
 * withdraw(): Prompts the user to enter their account number, PIN, and withdrawal amount, retrieves the corresponding BankAccount instance from the list, and withdraws the amount from the account if there are sufficient funds.
 * change_pin(): Prompts the user to enter their account number, current PIN, and new PIN, retrieves the corresponding BankAccount instance from the list, and changes the PIN.
 * exit(): Exits the program.

#### BankAccount Class:
The BankAccount class represents a bank account and contains information such as the account number, balance, and transaction history. The class contains the following methods:

__init__(self, account_number, balance): Initializes a new BankAccount instance with the specified account number and balance.
check_balance(): Returns the current balance of the account.
deposit(self, amount): Deposits the specified amount into the account and adds a new transaction to the transaction history.
withdraw(self, amount): Withdraws the specified amount from the account if there are sufficient funds and adds a new transaction to the transaction history.

#### Transaction Class:
The Transaction class represents a single transaction and contains information such as the type (deposit or withdrawal), amount, and date and time. The class contains the following methods:

__init__(self, transaction_type, amount, date_time): Initializes a new Transaction instance with the specified type, amount, and date and time.
