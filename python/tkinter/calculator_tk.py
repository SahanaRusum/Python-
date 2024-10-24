import tkinter as tk

def btn_click(item):
    input_field.insert(tk.END, str(item))

def btn_clear():
    input_field.delete(0, tk.END)

def btn_equal():
    try:
        result = str(eval(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")

input_field = tk.Entry(window, font=("Arial", 18), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_value = 1
col_value = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 18), command=btn_equal)
    elif button == "C":
        btn = tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 18), command=btn_clear)
    else:
        btn = tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda button=button: btn_click(button))
    
    btn.grid(row=row_value, column=col_value)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

window.mainloop()
