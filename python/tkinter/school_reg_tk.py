import tkinter as tk
root = tk.Tk()
root.title("School Registration Form")
root.geometry("400x400")
def show_custom_message(title, message):
    message_window = tk.Toplevel(root)
    message_window.title(title)
    message_window.geometry("300x150")
    
    tk.Label(message_window, text=message, padx=20, pady=20).pack()
    
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
    ok_button.pack(pady=10)

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    student_class = entry_class.get()
    subjects = entry_subjects.get()
    
    show_custom_message(
        "Form Submitted",
        f"Name: {name}\nAge: {age}\nClass: {student_class}\nSubjects: {subjects}"
    )
    
  

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_subjects.delete(0, tk.END)

label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

label_age = tk.Label(root, text="Age:")
label_age.pack(pady=5)
entry_age = tk.Entry(root, width=40)
entry_age.pack(pady=5)

label_class = tk.Label(root, text="Class:")
label_class.pack(pady=5)
entry_class = tk.Entry(root, width=40)
entry_class.pack(pady=5)

label_subjects = tk.Label(root, text="Subjects:")
label_subjects.pack(pady=5)
entry_subjects = tk.Entry(root, width=40)
entry_subjects.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.pack(pady=10)
root.mainloop()
