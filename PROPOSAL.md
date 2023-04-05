## COMP830 Software Development 
### Final Project Proposal
### Team Members:
`Dheeraj Kistapuram` | `Nikith Kaithalapuram` | `Sai Prakhyat Bommana`
### Project Name: ATM Stimulator
### Project Description: 
To create a python program that simulates the functionalities of an ATM machine, allowing users to perform financial transactions such as check balance, deposits, withdraw without physically visiting a bank.
### Project Complexity:
* User Interface - The user interface of an ATM simulator is critical to its success, and it can be complex to design and implement. 
* Security - Security is an essential aspect of an ATM simulator, and ensuring the system is secure can be complex. 
* Transaction Processing - The processing of ATM transactions can be complex, especially if the system needs to handle multiple types of transactions, including withdrawals, deposits, and balance inquiries.
* Testing and Validation - To ensure the system is working as intended, the project may require extensive testing and validation. This can include unit testing, integration testing, and end-to-end testing.

### Project Features: 
In this ATM simulator project, it contains classes for the ATM machine, bank account, and transactions. We are using the object-oriented programming concepts such as encapsulation, inheritance, and polymorphism to model these classes.
ATM class: This class will have methods to perform operations such as cash withdrawal, deposit, balance inquiry, and funds transfer. We can use design patterns such as State pattern to model the various states of the ATM machine.
BankAccount class: This class will have methods to perform operations such as checking the account balance, depositing money, and withdrawing money. We can use the Singleton pattern to ensure that only one instance of the BankAccount class exists at any time. 
Transaction class: This class will have methods to record the details of each transaction such as transaction type (withdrawal, deposit, transfer), transaction amount, transaction time, and transaction status. We can use the Observer pattern to notify the ATM machine and the bank account whenever a new transaction is recorded.
Finally, we can create a user interface using a GUI library such as Tkinter or PyQt to allow users to interact with the ATM simulator.
### Project Functionality:
•	The program should have a login system where users can input their ATM card number and PIN to access their account.
•	The program should allow users to perform various transactions such as cash withdrawals, deposits, balance inquiries, and funds transfer.
•	The program should have a user interface that displays the available options and prompts the user for inputs.
•	The program should have a system for error handling, such as displaying error messages when a user inputs incorrect information.
•	The program should keep track of each user's account balance and transaction history.
### Project Goals:
•	Able to create a login system that allows users to input their ATM card number and PIN to access their account.
•	Able to create a menu system that displays the available transaction options (cash withdrawals, deposits, balance inquiries, and funds transfer).
•	To Implement the functionalities for each transaction option, such as deducting funds for withdrawals and adding funds for deposits.
•	Able to create an error handling system that displays error messages for invalid inputs and prevents users from performing unauthorized transactions.
•	To Implement a system for tracking each user's account balance and transaction history, storing the data in a file or database.
### Project Tools: 
•	Python 3.10.7
•	PyCharm 2022.2.1 (Professional Edition)
•	GitHub
GitHub Repo Link: https://github.com/NIK8H/COMP830M1_Nikith_Dheeraj_Prakhyat
