class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odcmeter_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' ' + self.make + ' ' +self.model
        return long_name.title()

    def read_odcmeter(self):
        print("This car has "+str(self.odcmeter_reading)+" mils on it.")

    def update_odcmeter(self, mileage):
        self.odcmeter_reading = mileage

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odcmeter()

my_new_car.odcmeter_reading = 23
my_new_car.read_odcmeter()

my_new_car.update_odcmeter(26)
my_new_car.read_odcmeter()