import tkinter as tk


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")


def handle_account(account):
    def deposit():
        amount = float(deposit_entry.get())
        account.deposit(amount)
        deposit_entry.delete(0, tk.END)

    def withdraw():
        amount = float(withdraw_entry.get())
        account.withdraw(amount)
        withdraw_entry.delete(0, tk.END)

    account_window = tk.Toplevel()
    account_window.title("Bank Account")

    deposit_label = tk.Label(account_window, text="Deposit amount:")
    deposit_label.pack()

    deposit_entry = tk.Entry(account_window)
    deposit_entry.pack()

    deposit_button = tk.Button(account_window, text="Deposit", command=deposit)
    deposit_button.pack()

    withdraw_label = tk.Label(account_window, text="Withdraw amount:")
    withdraw_label.pack()

    withdraw_entry = tk.Entry(account_window)
    withdraw_entry.pack()

    withdraw_button = tk.Button(account_window, text="Withdraw", command=withdraw)
    withdraw_button.pack()


def main():
    root = tk.Tk()
    root.title("Virtual Bank App")

    def select_account(account):
        handle_account(account)

    current_account = BankAccount()
    savings_account = BankAccount()

    current_button = tk.Button(root, text="Current Account", command=lambda: select_account(current_account))
    current_button.pack()

    savings_button = tk.Button(root, text="Savings Account", command=lambda: select_account(savings_account))
    savings_button.pack()

    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()