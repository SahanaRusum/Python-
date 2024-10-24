class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def start(self):
        print("Car started")
        print("Car honks: Beep Beep!")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")
        print("Motorcycle pops a wheelie!")


my_car = Car()
my_motorcycle = Motorcycle()
my_car.start()
my_car.stop()

print()  

my_motorcycle.start()
my_motorcycle.stop()

