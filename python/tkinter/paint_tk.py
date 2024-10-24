import tkinter as tk
from tkinter import colorchooser

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")

        self.pen_color = "black"
        self.pen_size = 5

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.create_toolbar()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack()

        pen_btn = tk.Button(toolbar, text="Pen", command=self.use_pen)
        pen_btn.pack(side=tk.LEFT)

        brush_btn = tk.Button(toolbar, text="Brush", command=self.use_brush)
        brush_btn.pack(side=tk.LEFT)

        color_btn = tk.Button(toolbar, text="Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT)

        eraser_btn = tk.Button(toolbar, text="Eraser", command=self.use_eraser)
        eraser_btn.pack(side=tk.LEFT)

        size_label = tk.Label(toolbar, text="Size: ")
        size_label.pack(side=tk.LEFT)

        self.size_var = tk.IntVar(value=self.pen_size)
        size_spinbox = tk.Spinbox(toolbar, from_=1, to=10, textvariable=self.size_var, command=self.change_size)
        size_spinbox.pack(side=tk.LEFT)

    def use_pen(self):
        self.pen_color = "black"

    def use_brush(self):
        self.pen_color = "black"

    def choose_color(self):
        self.pen_color = colorchooser.askcolor()[1]

    def use_eraser(self):
        self.pen_color = "white"

    def change_size(self):
        self.pen_size = self.size_var.get()

    def paint(self, event):
        x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
        x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()



            
            



