import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear the current entry
    entry.insert(tk.END, current_text + value)  # Add the button value to the entry

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Initialize Tkinter window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget for displaying the numbers and result
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

# List of button labels for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Loop through button list to create buttons in grid
row_value = 1
col_value = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 16), command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 16), command=clear)
    else:
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 16), command=lambda b=button: on_button_click(b))

    btn.grid(row=row_value, column=col_value, padx=5, pady=5)

    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

root.mainloop()
