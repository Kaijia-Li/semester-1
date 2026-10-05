# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!

number1 = input("please enter the number1 : ")
number2 = input("please enter the number2 : ")
number = (number1 * number2)

if number.isdigit():
    print(number)
else:
    print("That is not a number")

#This is my original self-written code, which has errors due to my lack of practice. The following is the revised code I created with help from AI. Please see it for reference.

if number1.isdigit() and number2.isdigit():
    # convert string to integer
    num1 = int(number1)
    num2 = int(number2)
    result = num1 * num2
    print(result)
else:
    print("That is not a number")
