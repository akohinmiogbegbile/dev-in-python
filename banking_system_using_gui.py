import tkinter as tk
from tkinter import messagebox
import locale

# Set the locale for Nigerian Naira
locale.setlocale(locale.LC_ALL, 'en_NG')

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            messagebox.showwarning("Error", "Insufficient balance.")

    def get_balance(self):
        return self.balance

def deposit_money():
    amount = float(deposit_entry.get())
    account.deposit(amount)
    current_balance_label.config(text="Current Balance: %s" % format_currency(account.get_balance()))

def withdraw_money():
    amount = float(withdraw_entry.get())
    account.withdraw(amount)
    current_balance_label.config(text="Current Balance: %s" % format_currency(account.get_balance()))

def format_currency(amount):
    return locale.currency(amount, grouping=True)


account = BankAccount("fanda shenum", "2211230982", 1000.00)


window = tk.Tk()
window.title("Banking System")

account_name_label = tk.Label(window, text="Account Name:")
account_name_label.pack()
account_name = tk.Label(window, text=account.name)
account_name.pack()

account_number_label = tk.Label(window, text="Account Number:")
account_number_label.pack()
account_number = tk.Label(window, text=account.account_number)
account_number.pack()

current_balance_label = tk.Label(window, text="Current Balance: %s" % format_currency(account.get_balance()))
current_balance_label.pack()

deposit_label = tk.Label(window, text="Deposit Amount:")
deposit_label.pack()
deposit_entry = tk.Entry(window)
deposit_entry.pack()

withdraw_label = tk.Label(window, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = tk.Entry(window)
withdraw_entry.pack()

deposit_button = tk.Button(window, text="Deposit", command=deposit_money)
deposit_button.pack()

withdraw_button = tk.Button(window, text="Withdraw", command=withdraw_money)
withdraw_button.pack()

window.mainloop()