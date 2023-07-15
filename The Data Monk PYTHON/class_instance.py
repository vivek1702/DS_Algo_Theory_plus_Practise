# Define a class named car with 2 attributes, “color” and “speed”. Then create an
# instance and return speed.


class Car:
    def __init__(self, color, speed): #2 attributes created 
        self.c = color      #created instance c and s
        self.s = speed

car = Car("Red", '20mph')
print(car.s)

