#Q3 A
class Car:
    def __init__(self, year, model):
        self.year = year
        self.model = model
    
    def __str__(self) -> str:
        return self.year + " " + self.model

my_car = Car("1964", "Old")
print("my car is", my_car)

#there is no (self) and the error says that its looking for 3 arguments when the code only has 2


