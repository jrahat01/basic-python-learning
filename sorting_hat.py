Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
questionOne = int(input('Do you like Dawn or Dusk?'+'\n1) Dawn'+'\n2) Dusk\n'))


if (questionOne == 1):
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif (questionOne == 2):
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print('Wrong input')

questionTwo = int(input('When I\'m dead, I want people to remember me as:'+'\n1) The Good'+'\n2) The Great'+'\n3) The Wise'+'\n4) The Bold\n'))

if (questionTwo == 1):
  Hufflepuff = Hufflepuff + 2
elif (questionTwo == 2):
  Slytherin=Slytherin + 2
elif(questionTwo == 3):
  Ravenclaw=Ravenclaw + 2
elif(questionTwo == 4):
  Gryffindor=Gryffindor + 2
else:
  print('Wrong input')
questionThree = int(input('Which kind of instrument most pleases your ear?'+'\n1) The Violin'+'\n2) The Trumpet'+'\n3) The Piano'+'\n4) The Drum\n'))

if (questionThree == 1):
  Slytherin=Slytherin + 4
elif (questionThree == 2):
  Hufflepuff=Hufflepuff + 4
elif(questionThree == 3):
  Ravenclaw=Ravenclaw + 4
elif(questionThree == 4):
  Gryffindor=Gryffindor + 4
else:
  print('Wrong input')

print('Slytherin: ', Slytherin,'\n')
print('Hufflepuff: ', Hufflepuff ,'\n')
print('Ravenclaw: ', Ravenclaw ,'\n')
print('Gryffindor: ', Gryffindor ,'\n')

if (Slytherin >= Hufflepuff and Slytherin >= Ravenclaw and Slytherin >= Gryffindor):
  print('Slytherin!!')
elif(Hufflepuff >= Ravenclaw and Hufflepuff >= Gryffindor):
  print('Hufflepuff!!')
elif(Ravenclaw >= Gryffindor):
  print('Ravenclaw!!')
else:
  print('Gryffindor!!')