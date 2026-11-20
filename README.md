Python Banking System

A command-line banking application built with Python using Object-Oriented Programming (OOP). The project simulates basic banking operations, allowing users to create accounts, check account information, deposit funds, withdraw money, and initiate transfers.

Tech Stack

* Python – Core programming language.
* Object-Oriented Programming (OOP) – Account management through classes and methods.
* Random – Automatic generation of account numbers.
* SQLAlchemy – Imported for potential database integration.

Features

* Account Creation: Create new bank accounts with randomly generated account numbers.
* Account Information: Display account details, including account number, owner, PIN, and balance.
* Deposits: Add funds to an existing account.
* Withdrawals: Withdraw funds after account number and PIN verification.
* Transfers: Search for recipient accounts using their account numbers.
* Account Management: Store and manage account objects using Python lists.

Project Structure

banking-system/
│
└── main.py

Getting Started

1. Clone the repository

git clone <repository-url>
cd banking-system

2. Install dependencies

The current implementation primarily uses Python’s built-in libraries.

SQLAlchemy is imported in the project and can be installed using:

pip install sqlalchemy

3. Run the application

python main.py

How It Works

The application is built around an Account class, which represents individual bank accounts.

Each account contains:

Attribute	Description
account_number	Unique account identifier
name	Account owner’s name
pin	Account security PIN
balance	Current account balance
transaction_history	Transaction history placeholder

The Account class includes methods for displaying account information, depositing funds, withdrawing money, and initiating transfers.

A separate create_account() function handles account creation and stores newly created accounts in a shared list.

Current Development Status

This project is currently a work in progress. It focuses on implementing basic banking functionality and practicing object-oriented programming concepts in Python.

Potential future improvements:

* Persistent database storage using SQLAlchemy.
* Improved account authentication and PIN security.
* Complete deposit, withdrawal, and transfer validation.
* Transaction history tracking.
* Input validation and error handling.
* A graphical user interface or web-based interface.
