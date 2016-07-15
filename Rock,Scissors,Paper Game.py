from random import randint
t = ["Rock", "Scissors", "Paper"]
Computer = t[randint(0,2)]
print (Computer)

won = 0 
lose = 0
rate = 0

def error():
	while True:
		try:
			user = int(input("1: Rock, 2: Scissors, or 3: Paper? : "))
			if user in range(1,3):
				return number
			elif:
				raise IOError
			else:
				raise ValueError		
		except ValueError:
			print ("You did not enter an integer.")
		except IOError:
			print ("You are out of range.")

