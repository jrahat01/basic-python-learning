# While loop is like an if statement, runs the code if its true
#difference is a while loop keeps repeating as long as the condition is true
#if condition is false then skips over the block and moves on to the next lines, if true keeps looping
guess = 0
tries = 0

while guess != 6 and tries < 5 :
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')

#Starting with no guess and no tries, letting the user guess up to 5 tries, 
#if their guess is equal to 6 then they got it
#If their tries equal to 5 without guessing 6, then they lose and ran out of tries 