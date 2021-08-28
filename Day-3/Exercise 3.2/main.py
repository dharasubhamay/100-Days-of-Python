"""
## BMI Calculator 2.0

# Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.


The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. **underweight, normal weight,  overweight, obese, clinically obese**. 

# Example Input


weight = 85

height = 1.75


# Example Output

85 ÷ (1.75 x 1.75) =  27.755102040816325

Your BMI is 28, you are slightly overweight.

e.g. When you hit **run**, this is what should happen:   


The testing code will check for print output that is formatted like one of the lines below:


"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."

Hint

1. Try to use the **exponent** operator in your code.
2. Remember to **round** your result to the nearest whole number. 
3. Make sure you include the words in **bold** from the interpretations. 
"""

#  Don't change the code below 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#  Don't change the code above 

#Write your code below this line 

bmi = float(weight) / ((float(height)) ** 2)
final_bmi = round(bmi)

if(bmi < 18.5):
  s = "underweight"
elif(bmi>=18.5 and bmi<25):
  s = "normal weight"
elif(bmi >= 25 and bmi < 30):
  s = "slightly overweight"
elif(bmi>=30 and bmi < 35):
  s = "obese"
elif(bmi >= 35):
  s = "clinically obese"

msg = f"Your BMI is {final_bmi}, you are {s}."
print(msg)