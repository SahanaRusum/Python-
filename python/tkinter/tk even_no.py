import tkinter as tk

class FilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filter with Decorator")
        self.root.geometry("400x400")
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 
        self.setup_ui()

    @staticmethod
    def log_decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            print(f"Filtered result: {result}")
            return result
        return wrapper

    @log_decorator
    def filter_list(self):
        filtered_numbers_gen = (num for num in self.numbers if num % 2 == 0)
        
        filtered_numbers = list(filtered_numbers_gen)
        
     
        formatted_numbers = list(map(lambda x: f"Number: {x}", filtered_numbers))
        
        self.result_label.config(text="Filtered List: " + ", ".join(formatted_numbers))
        return filtered_numbers

    def run_filter(self):
        self.filter_list()

    def setup_ui(self):
        filter_button = tk.Button(self.root, text="Filter Even Numbers", command=self.run_filter)
        filter_button.pack(pady=20)

        self.result_label = tk.Label(self.root, text="Filtered List: []")
        self.result_label.pack(pady=20)

root = tk.Tk()
app = FilterApp(root)
root.mainloop()
