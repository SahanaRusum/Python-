"""
In a coding class the teacher has taught the kids about the python GUI and has now assigned the following task to the students

1) Create a random name picker from a given list of students

2) should have a button clicking on which a random name should be picked

3) Once the random name is picked the name should be removed from the list so 
that the name is not repeated and also the removed name should show in completed section
#create a GUI with two sections one to see the randomly generated name and the
#  other one to see the names that are generated randomly and which are not
#  suppose to be considered for generating randomly again.
"""
import tkinter as tk
import random

student_name_list=['Sahana','Alice','Shiva','Shruthi','Priya']
def pick_random_name():
    if student_name_list:
     selected_name=random.choice(student_name_list)
     student_name_list.remove(selected_name)
     picked_name_label.config(text=f"Picked Name is: {selected_name}")
     completed_name_listbox.insert(tk.END, selected_name)
    else:
        picked_name_label.config(text="No more names left")

root=tk.Tk()
root.title("Random Nmae Picker")
picked_name_label=tk.Label(root, text=" picked name: none",font=("Arial",12))
picked_name_label.pack(pady=20)
pick_button=tk.Button(root, text=" pick_random_name ",command= pick_random_name, font=("Arial",12))
picked_name_label.pack(pady=10)
completed_name_listbox=tk.Listbox(root, font=("Arial",14),height=8,width=20)
completed_name_listbox.pack(pady=10)

root.mainloop()