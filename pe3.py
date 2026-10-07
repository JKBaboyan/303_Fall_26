"""Pair Exercise 3: Caesar cipher functions and bank account classes."""

import datetime
import string


def encode(input_text, shift):
    """Return the lowercase alphabet and text shifted around that alphabet."""
    alphabet = list(string.ascii_lowercase)
    encoded = []
    for character in input_text.lower():
        if character in alphabet:
            position = (alphabet.index(character) + shift) % len(alphabet)
            encoded.append(alphabet[position])
        else:
            encoded.append(character)
    return alphabet, "".join(encoded)


def decode(input_text, shift):
    """Reverse a Caesar shift and return the decoded lowercase text."""
    return encode(input_text, -shift)[1]


class BankAccount:
    """An account that accepts deposits and withdrawals."""

    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()
        if not isinstance(creation_date, datetime.date):
            raise TypeError("creation_date must be a datetime.date.")
        if creation_date > datetime.date.today():
            raise Exception("The account creation date cannot be in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("A deposit cannot be negative.")
        else:
            self.balance += amount
        return self.view_balance()

    def withdraw(self, amount):
        if amount < 0:
            print("A withdrawal cannot be negative.")
        else:
            self.balance -= amount
        return self.view_balance()

    def view_balance(self):
        print(f"Account balance: ${self.balance:.2f}")
        return self.balance


class SavingsAccount(BankAccount):
    """Savings withdrawals require 180 days of account age and enough funds."""

    def withdraw(self, amount):
        age = (datetime.date.today() - self.creation_date).days
        if amount < 0:
            print("A withdrawal cannot be negative.")
        elif age < 180:
            print("Savings withdrawals require an account age of 180 days.")
        elif amount > self.balance:
            print("Savings accounts cannot be overdrawn.")
        else:
            self.balance -= amount
        return self.view_balance()


class CheckingAccount(BankAccount):
    """Checking withdrawals charge $30 whenever they leave a negative balance."""

    def withdraw(self, amount):
        if amount < 0:
            print("A withdrawal cannot be negative.")
        else:
            self.balance -= amount
            if self.balance < 0:
                self.balance -= 30
        return self.view_balance()
