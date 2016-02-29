# "Tom's Racing Simulator" by Tvon256


from random import randint
import time


class Car(object):
	chance_of_winning = 0
	races_won = 0
	def __init__ (self, name, top_speed, acceleration, luck):
		self.name = name
		self.top_speed = top_speed
		self.acceleration = acceleration
		self.luck = luck
		
def race_logic(car1, car2):
	
	random_events = ["skidded of a cliff", "got hit by oncoming traffic", "got pulled over for speeding"]
	distance = randint(1,3)
	car1_score = 0
	car2_score = 0
	car1.chance_of_winning = 0
	car2.chance_of_winning = 0
	print ("Distance: " + str(distance))
	if (distance == 1):
		if car1.acceleration - car2.acceleration >= 1:
			car1.chance_of_winning = car1.chance_of_winning + 1
			print(car1.name + " gained 1 point from acceleration")
			time.sleep(1)
		elif car2.acceleration - car1.acceleration >= 1:
			car2.chance_of_winning = car2.chance_of_winning + 1
			print(car2.name + " gained 1 point from acceleration")
			time.sleep(1)
		if (car1.top_speed - car2.top_speed > 3):
			car1.chance_of_winning = car1.chance_of_winning + 2
			print(car1.name + " gained 2 points from top speed")
			time.sleep(1)
		elif (car2.top_speed - car1.top_speed > 3):
			car2.chance_of_winning = car2.chance_of_winning + 2
			print(car2.name + " gained 2 points from top speed")
			time.sleep(1)
	if (distance == 2):
		if car1.acceleration - car2.acceleration >= 2:
			car1.chance_of_winning = car1.chance_of_winning + 1
			print(car1.name + " gained 1 point from acceleration")
			time.sleep(1)
		elif car2.acceleration - car1.acceleration >= 2:
			car2.chance_of_winning = car2.chance_of_winning + 1
			print(car2.name + " gained 1 point from acceleration")
			time.sleep(1)
		if (car1.top_speed - car2.top_speed > 2):
			car1.chance_of_winning = car1.chance_of_winning + 2
			print(car1.name + " gained 2 points from top speed")
			time.sleep(1)
		elif (car2.top_speed - car1.top_speed > 2):
			car2.chance_of_winning = car2.chance_of_winning + 2
			print(car2.name + " gained 2 points from top speed")
			time.sleep(1)
	if (distance == 3):
		if car1.acceleration - car2.acceleration > 3:
			car1.chance_of_winning = car1.chance_of_winning + 2
			print(car1.name + " gained 2 points from acceleration")
			time.sleep(1)
		elif car2.acceleration - car1.acceleration > 3:
			car2.chance_of_winning = car2.chance_of_winning + 2
			print(car2.name + " gained 2 points from acceleration")
			time.sleep(1)
		if (car1.top_speed - car2.top_speed >= 1):
			car1.chance_of_winning = car1.chance_of_winning + 1
			print(car1.name + " gained 1 point from top speed")
			time.sleep(1)
		elif (car2.top_speed - car1.top_speed >= 1):
			car2.chance_of_winning = car2.chance_of_winning + 1
			print(car2.name + " gained 1 point from top speed")
			time.sleep(1)
	
	if (randint(0,5) == 5):
		print ("%s %s" % (car1.name, random_events[randint(0,2)]))
		car1.chance_of_winning = -10
	elif (randint(0,5) == 0):
		print ("%s %s" % (car2.name, random_events[randint(0,2)]))
		car2.chance_of_winning = -10
	
	print ("%s's score before luck: %s" % (car1.name, str(car1.chance_of_winning)))
	print ("%s's score before luck: %s" % (car2.name, str(car2.chance_of_winning)))
	
	car1_score = car1.chance_of_winning + randint(1,3) + car1.luck
	car2_score = car2.chance_of_winning + randint(1,3) + car2.luck
	
	print ("%s's score after luck: %s" % (car1.name, str(car1_score)))
	print ("%s's score after luck: %s" % (car2.name, str(car2_score)))
	
	if (car1_score > car2_score):
		winner = str(car1.name)
		car1.races_won = car1.races_won + 1
	elif (car2_score > car1_score):
		winner = str(car2.name)
		car2.races_won = car2.races_won + 1
	else:
		winner = "tie"
	return winner
		
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
		time.sleep(2)
		print ("Race %s. Winner: %s" % (str(counter), race_logic(p1_car, p2_car)))
		counter = counter + 1
		
		
	if (p1_car.races_won > p2_car.races_won):
		print("%s Has Won!" % (str(p1_car.name)))
	elif (p2_car.races_won > p1_car.races_won):
		print ("%s Has Won!" % (str(p2_car.name)))
	else:
		print ("It was a tie!")
	

while (1 == 1):			
	main_game()