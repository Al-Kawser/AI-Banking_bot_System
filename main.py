import random
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image

class BankingBot:
    def __init__(self):
        self.greetings = ['Hello!', 'Hi there!', 'Welcome!', 'Greetings!']
        self.goodbyes = ['Goodbye!', 'See you!', 'Bye!', 'Take care!']
        self.balance = 0
        self.statements = []

    def get_greeting(self):
        return random.choice(self.greetings)

    def get_goodbye(self):
        return random.choice(self.goodbyes)

    def check_balance(self):
        return f"Your current balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        statement = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'description': f"Deposit of ${amount}",
        }
        self.statements.append(statement)
        return f"You have deposited ${amount}. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            statement = {
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'description': f"Withdrawal of ${amount}",
            }
            self.statements.append(statement)
            return f"You have withdrawn ${amount}. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds"

    def view_statements(self):
        if len(self.statements) == 0:
            return "No statements available"
        else:
            statement_str = ""
            for statement in self.statements:
                statement_str += f"{statement['date']} - {statement['description']}\n"
            return statement_str

    def answer_basic_questions(self, question):
        if 'bank' in question:
            return "Our bank is committed to providing exceptional financial services and personalized solutions to our customers."
        elif 'current account' in question:
            return "A current account is a type of bank account that is typically used for day-to-day transactions. It allows you to deposit and withdraw money as needed, write checks, and may offer additional features like an overdraft facility."
        elif 'savings account' in question:
            return "A savings account is a type of bank account designed for saving money over time. It usually offers interest on the deposited funds, helping them grow. Savings accounts often have restrictions on the number of withdrawals per month and may require maintaining a minimum balance."
        else:
            return "I'm sorry, I don't have information about that topic."

class BankingBotGUI:
    def __init__(self, root):
        self.root = root
        self.bot = BankingBot()
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("Banking Bot")


        background_image = Image.open("images/bank.jpg")
        background_image = background_image.resize((1500, 800), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.greeting_label = tk.Label(self.root, text=self.bot.get_greeting(), font=("Arial", 18, "bold"))
        self.greeting_label.pack()

        self.input_label = tk.Label(self.root, text="What would you like to do?", font=("Arial", 12))
        self.input_label.pack()

        self.user_input_entry = tk.Entry(self.root, font=("Arial", 12))
        self.user_input_entry.pack()

        self.output_text = tk.Text(self.root, height=10, width=50, font=("Arial", 12))
        self.output_text.pack()

        self.submit_button = tk.Button(self.root, text="Submit!", font=("Arial", 12), command=self.process_user_input)
        self.submit_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit!", font=("Arial", 12), command=self.root.quit)
        self.exit_button.pack()

    def process_user_input(self):
        user_input = self.user_input_entry.get()

        if user_input.lower() == 'balance':
            output = self.bot.check_balance()
        elif user_input.lower().startswith('deposit'):
            amount = float(user_input.split()[1])
            output = self.bot.deposit(amount)
        elif user_input.lower().startswith('withdraw'):
            amount = float(user_input.split()[1])
            output = self.bot.withdraw(amount)
        elif user_input.lower() == 'statements':
            output = self.bot.view_statements()
        elif '?' in user_input:
            output = self.bot.answer_basic_questions(user_input)
        elif user_input.lower() == 'exit':
            output = self.bot.get_goodbye()
            self.root.quit()
        else:
            output = "Invalid input. Please try again."

        self.output_text.insert(tk.END, output + "\n")
        self.user_input_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    bot_gui = BankingBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
