def oddOrEven(number):
	''' takes in a positive integer or zero as a parameter and returns whether the number is odd or even '''
	if number % 2 == 0:
		return True
	else:
		return False


def numberOfDigits(number):
	''' takes a non-negative integer as a parameter and returns the number of digits in it '''
	number = str(number)
	return len(number)


def sumDigits(number):
	''' takes a non-negative integer as a parameter and returns the sum of its digits '''
	sum = 0
	number = str(number)
	for chr in number:
		chr = int(chr)
		sum += chr
	return sum
	

def sum_less_ints(number):
	''' takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number
		For example: sum_less_ints(3) → 3, which is 1 + 2; sum_less_ints(5) → 10, which is 1 + 2 + 3 + 4 '''
	sum = 0
	while number != 0:
		number -= 1
		sum += number	
	return sum


def factorial(number):
	''' takes a non-negative integer as a parameter and returns its factorial '''
	total = 1
	if number == 0:
		return 1
	else:
		while number > 0:
			total = total * number
			number -= 1
		return total


def divisibleBy(number1, number2): 
	''' takes two positive integers as parameters and figures out whether the second number is a factor of the first.
		In other words, returns true if the second number divides into the first number evenly, and false otherwise '''
	if number1 % number2 == 0:
		return True
	else:
		return False


def primeNumber(number):
	''' takes a positive integer as a parameter and returns whether the number is a prime '''
	if number == 0 or number == 1:
		return False
	else:
		for num in range(2, number):
			if (number % num) == 0:
				return False
			else:
				return True

		newNumber = number - 1
		while newNumber != 1:
			try: 
				int(number / newNumber)
			except ValueError:
				newNumber -= 1
				if newNumber == 1:
					return True
			else:
				return False
					

def perfectNumber(number):
	''' takes a positive integer as a parameter and returns whether the number is perfect.
		A perfect number is a number that equals the sum of its proper factors. 
		A proper factor is any factor except the number itself.  
		For example: isPerfect(6) → True, because 6 = 1 + 2 + 3. '''
	perfectNumbers = []
	perfectNumbers.append(6)
	perfectNumbers.append(28)
	perfectNumbers.append(496)
	perfectNumbers.append(8128)
	perfectNumbers.append(33550336)
	perfectNumbers.append(8589869056)
	perfectNumbers.append(137438691328)
	perfectNumbers.append(2305843008139952128)
	if number in perfectNumbers:
		return True
	else:
		return False
	
	
def sumDigitsDivisible(number):
	''' takes a positive integer and returns true if the sum of the digits of the number divides evenly into the number, false otherwise.
		calls the sumDigits function to define this function '''
	sumOfDigits = sumDigits(number)
	if sumOfDigits == 0:
		return False
	elif number % sumOfDigits != 0:
		return False
	else:
		return True