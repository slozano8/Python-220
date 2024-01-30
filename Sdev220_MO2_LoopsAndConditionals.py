#4.1 Write the conditional tests (if, else, and elif) to print the string 'too low' 
# if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.

#Using variables secret and guess.
secret = 9
guess = 4
print("\nAssignment 4.13")
# using else, if and elif to print string.

if guess < secret:
  print(" Too low.")
elif guess > secret:
  print(" Too high.")
elif guess  == secret:
     print(" Just right")
print()
#4.1 BUG REPORT: without an input string it would just print "too low" 
  
  
#4.2 Assign True or False to the variables small and green.
# Variables
small = True
green = False
# Write some if/else statements to print which of these matches those choices:
#cherry, pea, watermelon and pumpkin.
print("\nAssignment 4.2")
if small and not green:
  print("Cherry")
elif small and green:
  print("Pea")
elif not small and green:
  print("Watermelon")
elif not small and not green:
  print("Pumpkin")
print()

#6.1 Use a for loop to print the values of the list [3, 2, 1, 0].
#BUG REPORT: This one was self explanatory. no problem
ListOne = [3, 2, 1, 0]
for index in ListOne:
    print(index)
    
    
#6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number.
# Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. 
# If number equals guess_me, print 'found it!' and then exit the loop.
# If number is greater than guess_me, print 'oops' and then exit the loop. 
# Increment number at the end of the loop.
guess_me = 7
number = 1
print("\nAssignment 6.2")
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1
  
print()
   
#6.3 Assign the value 5 to the variable guess_me.
# Use a for loop to iterate a variable called number over range(10). 
# If number is less than guess_me, print 'too low'. If it equals guess_me,
# print found it! and then break out of the for loop.
#If number is greater than guess_me, print 'oops' and then exit the loop.

#BUG REPORT: very similar to the last one, run at first try
print("\nAssignment 6.3")
guess_me = 9

for number in range(10):    
    if number < guess_me:
        print("too low")  
    elif number == guess_me:
        print("found it!")
        break
    else: 
        print("oops")
        break
        