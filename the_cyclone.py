#and returns true if ONLY BOTH conditions are true, or returns true if ONLY ONE condition is true, both are false if otherwise
#not returns true if the condition IS FALSE, and vice versa

height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif credits < 10 and height >= 137:
  print("You don't have enough credits to ride.")
else:
  print("You are not tall enough for this ride, nor do you have enough credits.")
