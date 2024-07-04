import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        self.root.config(bg="#F0F0F0")

        self.create_widgets()

    def create_widgets(self):
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 14)
        button_font = ("Helvetica", 14, "bold")

        input_frame = tk.Frame(self.root, bg="#F0F0F0")
        input_frame.pack(pady=20)

        operation_frame = tk.Frame(self.root, bg="#F0F0F0")
        operation_frame.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#F0F0F0")
        button_frame.pack(pady=20)

        result_frame = tk.Frame(self.root, bg="#F0F0F0")
        result_frame.pack(pady=10)
        self.num1_label = tk.Label(input_frame, text="Enter first number:", font=label_font, bg="#F0F0F0")
        self.num1_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')

        self.num1_entry = tk.Entry(input_frame, font=entry_font, width=15)
        self.num1_entry.grid(row=0, column=1, pady=5, padx=5)

        self.num2_label = tk.Label(input_frame, text="Enter second number:", font=label_font, bg="#F0F0F0")
        self.num2_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

        self.num2_entry = tk.Entry(input_frame, font=entry_font, width=15)
        self.num2_entry.grid(row=1, column=1, pady=5, padx=5)
        self.operation_label = tk.Label(operation_frame, text="Select operation:", font=label_font, bg="#F0F0F0")
        self.operation_label.pack(side=tk.LEFT, padx=5)

        self.operation_var = tk.StringVar(value="Add")
        self.operation_menu = tk.OptionMenu(operation_frame, self.operation_var, "Add", "Subtract", "Multiply", "Divide")
        self.operation_menu.config(font=entry_font, width=10)
        self.operation_menu.pack(side=tk.LEFT, padx=5)
        self.calculate_button = tk.Button(button_frame, text="Calculate", font=button_font, bg="#4CAF50", fg="white", command=self.calculate)
        self.calculate_button.pack(fill=tk.X, padx=20)

        self.result_label = tk.Label(result_frame, text="Result: ", font=label_font, bg="#F0F0F0")
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
            else:
                result = "Invalid operation"

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()