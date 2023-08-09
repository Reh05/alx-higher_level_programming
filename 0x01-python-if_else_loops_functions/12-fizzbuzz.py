#!/usr/bin/python3
def fizzbuzz():
	if input % 3 == 0 and input % 5 == 0:
		print("FizzBuzz", end="")
	elif input % 3 == 0:
		print("Fizz", end="")
	elif input % 5 == 0:
		print("Buzz", end="")
	else:
		print("{}".format(input), end="")
