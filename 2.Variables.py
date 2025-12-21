# Variables: these are used to store your data in python or hold your data
# like in maths where we used x = 10 or y = 9, variables are same here in python too
#learning to name variables:

name = 'sanket' #using albhabet is valid
user_id = 2 # using uderscore (_) to seperate words is valid
num1 = 23 # using number after is valid

# but

'''
we cannot use these:
- 1name = 'sanket'(a variable name cannot start with a number)
- last name = 'shrestha'(we cannot leave space in name called white space)
'''

# variables are case sensitives(uppercase and lowercase matters)
first_name = 'Sanket'  # 'first_name' and 'First_name' are different variables
First_name = 'Sanket'  # Another variable with a different case
print(first_name)  # Output: Sanket
print(First_name)  # Output: Sanket

#You cannot use Python's reserved keywords as variable names4
# def = 10  # INVALID, 'def' is a keyword in Python
# You should avoid using Python's reserved words like: True, False, if, else, etc.

# Variable names should be descriptive and meaningful
user_name = 'Sanket'  # Meaningful variable name, tells us what the value is
total_score = 95      # Descriptive of what the variable holds