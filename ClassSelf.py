class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

class ElectricCar(Car):
    def __init__(self, brand,model)



my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(my_new_car.brand)