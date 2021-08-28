"""
## Pizza Order

# Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1


# Example Input


size = "L"

add_pepperoni = "Y"

extra_cheese = "N"


# Example Output

Your final bill is: $28.

e.g. When you hit **run**, this is what should happen:  

 

# Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
"""

#  Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#  Don't change the code above 

#Write your code below this line 

if(size == "S"):
  cost1 = 15
elif(size == "M"):
  cost1 = 20
elif(size == "L"):
  cost1 = 25

if(add_pepperoni == "Y"):
  if(size == "S"):
    cost2 = 2
  else:
    cost2 = 3
else:
  cost2 = 0

if(extra_cheese == "Y"):
  cost3 = 1
else:
  cost3 = 0

final_cost = cost1 + cost2 + cost3

print(f"Your final bill is: ${final_cost}.")