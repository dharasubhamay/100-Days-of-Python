"""
## Prime Numbers

# Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1. 


**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Here are the numbers up to 100, prime numbers are highlighted in yellow:

# Example Input 1

73

# Example Output 1

It's a prime number.

# Example Input 2


75

# Example Output 2

It's not a prime number.

# Hint

1. Remember the modulus: 

2. Make sure you name your function/parameters the same as when it's called on the last line of code. 

3. Use the same wording as the Example Outputs to make sure the tests pass. 
"""

#Write your code below this line 
from math import sqrt

def prime_checker(number):
  prime_flag = 0
  if number>1 :
    for i in range(2, (int(sqrt(number)) + 1)):
      if number%i == 0:
        prime_flag = 1
        break
    if prime_flag == 0:
      print("It's a prime number.")
    else:
      print("It's not a prime number.") 
  else:
    print("It's not a prime number.")

#Write your code above this line 
    
#Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)