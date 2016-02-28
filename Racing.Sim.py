# "Tom's Racing Simulator" by Tvon256


from random import randint
import time

distance = randint(1,3)

class Car(object):
	chance_of_winning = 0
	races_won = 0
	def __init__ (self, name, top_speed, acceleration, luck):
		self.name = name
		self.top_speed = top_speed
		self.acceleration = acceleration
		self.luck = luck
		
	
def main_game ():
	print ("#############################################################")
	print("Welcome To Tom's Racing Simulator")
	print("You will each be given a car with a random set of attributes")
	print("Whichever of these cars wins 2 out of 3 races wins the game!")
	
	p1_name = input("Enter P1's Name: ")
	p2_name = input("Enter p2's Name: ")
	
	p1_car = Car(p1_name, randint(1,5), randint(1,5), randint(1,3))
	print ("%s : Top Speed = %s, Acceleration = %s, luck = %s" % (str(p1_car.name), str(p1_car.top_speed), str(p1_car.acceleration), str(p1_car.luck)))
	p2_car = Car(p2_name, randint(1,5), randint(1,5), randint(1,3))
	print ("%s : Top Speed = %s, Acceleration = %s, luck = %s" % (str(p2_car.name), str(p2_car.top_speed), str(p2_car.acceleration), str(p2_car.luck)))
	
	counter = 1
	while counter <= 3:
		print ("Race %s over a distance of %s. Winner: %s" % (str(distance), str(counter), race_logic(p1_car, p2_car)))
		counter = counter + 1
		time.sleep(2)
		
	if (p1_car.races_won > p2_car.races_won):
		print("%s Has Won!" % (str(p1_car.name)))
	elif (p2_car.races_won > p1_car.races_won):
		print ("%s Has Won!" % (str(p2_car.name)))
	else:
		print ("It was a tie!")
	
def race_logic(car1, car2):
	
	if (distance == 1):
		if car1.acceleration - car2.acceleration >= 1:
			car1.chance_of_winning = car1.chance_of_winning + 1
		elif car2.acceleration - car1.acceleration >= 1:
			car2.chance_of_winning = car2.chance_of_winning + 1
		if (car1.top_speed - car2.top_speed > 3):
			car1.chance_of_winning + car1.chance_of_winning + 2
		elif (car2.top_speed - car1.top_speed > 3):
			car2.chance_of_winning + car2.chance_of_winning + 2
	if (distance == 2):
		if car1.acceleration - car2.acceleration >= 2:
			car1.chance_of_winning = car1.chance_of_winning + 1
		elif car2.acceleration - car1.acceleration >= 2:
			car2.chance_of_winning = car2.chance_of_winning + 1
		if (car1.top_speed - car2.top_speed > 2):
			car1.chance_of_winning + car1.chance_of_winning + 2
		elif (car2.top_speed - car1.top_speed > 2):
			car2.chance_of_winning + car2.chance_of_winning + 2
	if (distance == 3):
		if car1.acceleration - car2.acceleration > 3:
			car1.chance_of_winning = car1.chance_of_winning + 2
		elif car2.acceleration - car1.acceleration > 3:
			car2.chance_of_winning = car2.chance_of_winning + 2
		if (car1.top_speed - car2.top_speed >= 1):
			car1.chance_of_winning + car1.chance_of_winning + 1
		elif (car2.top_speed - car1.top_speed >= 1):
			car2.chance_of_winning + car2.chance_of_winning + 1
	
	car1_score = car1.chance_of_winning + randint(1,3) + car1.luck
	car2_score = car2.chance_of_winning + randint(1,3) + car2.luck
	
	if (car1_score > car2_score):
		winner = str(car1.name)
		car1.races_won = car1.races_won + 1
	elif (car2_score > car1_score):
		winner = str(car2.name)
		car2.races_won = car2.races_won + 1
	else:
		winner = "tie"
	return winner
while (1 == 1):			
	main_game()