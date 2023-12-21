#Assignment 3
#Anasuya Sikdar
import random

def play(num):
    'Game based on Guessing alphabet from book'
    fname = 'Pride_and_Prejudice.txt'
    infile = open(fname,'r')
    s = infile.read()
    infile.close()
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
    for i in range(num):
        isValid = True
        letter_1 = random.choice(alphabet)
        letter_2 = random.choice(alphabet)
        
        user_input = input(f'Which letter occurs more often "{letter_1}" or "{letter_2}"?')
        
        if user_input not in [letter_1, letter_2]:
            isValid = False
            print(f'"{user_input}" is not one of the choice letters')
        else:
          if not user_input.isalpha():
              isValid = False
              print(f'"{user_input}" is not a letter')
              
          if letter_1 == letter_2:
              print('The letters are the same \n"{}" occurs {} times'.format(letter_1, s.count(letter_1)))
              
          if isValid:
              count1 = s.count(letter_1)
              count2 = s.count(letter_2)

              if count1 > count2 and letter_1 == user_input:
                  print('Correct: "{}" occurs {} times and "{}" occurs {} times'.format(letter_1, count1, letter_2, count2))
              elif count2 > count1 and letter_2 == user_input:
                  print('Correct: "{}" occurs {} times and "{}" occurs {} times'.format(letter_2, count2, letter_1, count1))
              elif count1 == count2:
                  print('Correct: Both letters occur the same number of times, {} times each.'.format(count1))
              else:
                  print('Incorrect: "{}" occurs {} times and "{}" occurs {} times'.format(letter_1, count1, letter_2, count2))
    
    print("Goodbye")
