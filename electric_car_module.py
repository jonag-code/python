#Note in this module we import the class Car() from
# another module! ...i.e. the file "car_module.py" 
from car_module import Car

class Battery():
	def __init__(self, battery_size):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a %s-kWh battery." %self.battery_size)

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

#------------------------------------------------------------------------
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery(70)