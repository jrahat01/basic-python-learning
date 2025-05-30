import random


question = input('Ask a yes or no question: ')
num = random.randint(1,9)
if (num == 1):
  print('Question: '+ question +'\nMagic 8 Ball: Yes - definitely')
elif(num == 2):
  print('Question: '+ question +'\nMagic 8 Ball: It is decidedly so.')
elif(num == 3):
  print('Question: '+ question +'\nMagic 8 Ball: Without a doubt.')
elif(num == 4):
  print('Question: '+ question +'\nMagic 8 Ball: Reply Hazy. try again.')
elif(num == 5):
  print('Question: '+ question +'\nMagic 8 Ball: Ask again later.')
elif(num == 6):
  print('Question: '+ question +'\nMagic 8 Ball: Better not tell you now.')
elif(num == 7):
  print('Question: '+ question +'\nMagic 8 Ball: My sources say no.')
elif(num == 8):
  print('Question: '+ question +'\nMagic 8 Ball: Outlook not so good.')
else:
  print('Question: '+ question +'\nMagic 8 Ball: Very doubtful.')

