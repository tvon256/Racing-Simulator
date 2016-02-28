from random import randint

class Car(object):
	def __ini__ (self, name, top_speed, acceleration, luck):
		self.name = name
		self.top_speed = top_speed
		self.acceleration = acceleration
		self.luck = luck
		
def make_cars (p1, p2):
	p1_car = Car(p1, randint(1,5), randint(1,5), randint(1,3))
	p2_car = Car(p2, randint(1,5), randint(1,5), randint(1,3))