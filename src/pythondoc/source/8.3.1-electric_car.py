class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    # 子类的方法 子 __init__()
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # 给子类定义属性
        self.battery_size = 70

    # 给子类定义方法
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+ "-kwh battery.")

my_tesla = ElectricCar('testla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()