class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def setLength(self,length):
        self.length=length
    def setBreadth(self,breadth):
        self.breadth=breadth
    def getArea(self):
        return self.length * self.breadth
    def getPerimeter(self):
        return 2*(self.length+self.breadth)
class square(rectangle):
    def __init__(self,side):
        self.side=side
        self.length=side
        self.breadth=side
    def setLength(self,side):
        self.side=side
        self.length=side
        self.breadth=side
    def setBreadth(self,side):
        self.side=side
        self.length=side
        self.breadth=side
    def setSide(self,side):
        self.setLength(side)
    def getArea(self):
        return self.side*self.side
    def getPerimeter(self):
        return 4*(self.side)

shape_type = input("Would you like to create a Rectangle or Square? ").strip().lower()

if shape_type == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    rectangle = rectangle(length, breadth)
    print('Rectangle Area', rectangle.getArea())
    print('Rectangle Perimeter', rectangle.getPerimeter())

elif shape_type == "square":
    side = float(input("Enter the side length of the square: "))
    square = square(side)
    print('Square Area', square.getArea())
    print('Square Perimeter', square.getPerimeter())

    change_side = input("Would you like to change the side length of the square? (yes/no) ").strip().lower()
    if change_side == "yes":
        new_side = float(input("Enter the new side length of the square: "))
        square.setSide(new_side)
        print('Updated Square Area', square.getArea())
        print('Updated Square Perimeter', square.getPerimeter())

else:
    print("Invalid shape type. Please enter 'Rectangle' or 'Square'.")



    
    