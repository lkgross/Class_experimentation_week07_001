# Variable assignment
car = 'bmw'
print(type(car))
print(car == 'audi')
print(car != 'audi')
print('Enter Q to quit.')
user_response = 'q'
if user_response.upper() == 'Q':
    print("Quitting")
age = 18
print(age == 18)
print(True and True)
# For (cond1 and cond2) to be True,
# then cond1 must be True and
# cond2 must be True
print(3 >= 3 and 5 >= 3)
# Say 3 is less than or equal to 3 and 5
print(3 <= 3 and 3 <= 5)
# For (cond1 or cond2) to be True,
# then cond1 or cond2 or both must be True.
print(3 > 3 or 3 >= 3)
print(not(True))
print(not(car == 'bmw'))
print(not(False))
print(not(car == 'audi'))
# We can start and end a multi-line comment
# with '''
'''
print()
print("First try.")
print("Do you want to continue? Y/N")
user_response = 'Y'
if user_response == 'Y':
    print("Let's continue!")

print()
print("Next try.")
user_response = 'N'
if user_response == 'Y':
    print("Let's continue!")

print()
print("Next try.")
user_response = 'y'
if user_response == 'Y':
    print("Let's continue!")
    print("Let's play some more.")
   
print()
print("Next try.")
user_response = 'Y'
if user_response == 'Y':
    print("Let's continue!")
print("Let's play some more.")

print()
print("Next try.")
user_response = 'Y'
if user_response == 'Y':
    print("Let's continue!")
if user_response != 'Y':
    print("Let's quit.")

# Try if-else.
print()
print("Next try.")
user_response = 'Y'
if user_response == 'Y':
    print("Let's continue!")
# Otherwise...
else:
    print("Let's quit.")

# Try if-else.
print()
print("Next try.")
user_response = 'N'
if user_response == 'Y':
    print("Let's continue!")
# Otherwise...
else:
    print("Let's quit.")

# Try if-else.
print()
print("Next try.")
user_response = 'yes'
if user_response == 'Y':
    print("Let's continue!")
# Otherwise...
else:
    print("Let's quit.")
'''

# Try if-else.
print()
print("Next try.")
user_response = 'yes'
if user_response == 'Y':
    print("Let's continue!")
# Otherwise if...
elif (user_response == "N"):
    print("Let's quit.")
else:
    print("Error!")
