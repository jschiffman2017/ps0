import ps0

number = 1
oddEven = ps0.oddOrEven(number)
print("{} is even: {}".format(number, oddEven))
number = 2
oddEven = ps0.oddOrEven(number)
print("{} is even: {}".format(number, oddEven))
number = 0
oddEven = ps0.oddOrEven(number)
print("{} is even: {}".format(number, oddEven))


number = 1
numDigits = ps0.numberOfDigits(number)
print("{} has {} digits.".format(number, numDigits))
number = 15
numDigits = ps0.numberOfDigits(number)
print("{} has {} digits.".format(number, numDigits))
number = 0
numDigits = ps0.numberOfDigits(number)
print("{} has {} digits.".format(number, numDigits))


number = 0
sum = ps0.sumDigits(number)
print("The sum of {}'s digits is {}.".format(number, sum))
number = 1
sum = ps0.sumDigits(number)
print("The sum of {}'s digits is {}.".format(number, sum))
number = 15
sum = ps0.sumDigits(number)
print("The sum of {}'s digits is {}.".format(number, sum))

number = 0
sumLess = ps0.sum_less_ints(number)
print("The sum of all the integers less than {} is {}.".format(number, sumLess))
number = 1
sumLess = ps0.sum_less_ints(number)
print("The sum of all the integers less than {} is {}.".format(number, sumLess))
number = 5
sumLess = ps0.sum_less_ints(number)
print("The sum of all the integers less than {} is {}.".format(number, sumLess))

number = 0
fac = ps0.factorial(number)
print("{} factorial is {}.".format(number, fac))
number = 1
fac = ps0.factorial(number)
print("{} factorial is {}.".format(number, fac))
number = 5
fac = ps0.factorial(number)
print("{} factorial is {}.".format(number, fac))

number = 0
prime = ps0.primeNumber(number)
print("{} is prime: {}".format(number, prime))
number = 1
prime = ps0.primeNumber(number)
print("{} is prime: {}".format(number, prime))
number = 3
prime = ps0.primeNumber(number)
print("{} is prime: {}".format(number, prime))
number = 4
prime = ps0.primeNumber(number)
print("{} is prime: {}".format(number, prime))

number = 0
perfect = ps0.perfectNumber(number)
print("{} is perfect: {}".format(number, perfect))
number = 1
perfect = ps0.perfectNumber(number)
print("{} is perfect: {}".format(number, perfect))
number = 6
perfect = ps0.perfectNumber(number)
print("{} is perfect: {}".format(number, perfect))


number = 0
sumDivisible = ps0.sumDigitsDivisible(number)
print("{} is divisible by the sum of its digits: {}".format(number, sumDivisible))
number = 1
sumDivisible = ps0.sumDigitsDivisible(number)
print("{} is divisible by the sum of its digits: {}".format(number, sumDivisible))
number = 12
sumDivisible = ps0.sumDigitsDivisible(number)
print("{} is divisible by the sum of its digits: {}".format(number, sumDivisible))
number = 15
sumDivisible = ps0.sumDigitsDivisible(number)
print("{} is divisible by the sum of its digits: {}".format(number, sumDivisible))


number = 1
divisor = 1
divisible = ps0.divisibleBy(number, divisor)
print("{} is divisible by {}: {}".format(number, divisor, divisible))
divisor = 2
divisible = ps0.divisibleBy(number, divisor)
print("{} is divisible by {}: {}".format(number, divisor, divisible))
number = 4
divisible = ps0.divisibleBy(number, divisor)
print("{} is divisible by {}: {}".format(number, divisor, divisible))