"""
Name(s): Sydney Bratton and Logan Lee
Name of Project: WORDLE
"""
import random
listofwords = ["earth", "final", "edict", "joust", "query"]
word = random.choice(listofwords) #picks a random word from the listofwords
print("Welcome to WORDLE 2.0") 
print("Here, you will have 6 tries to guess a 5 letter word, and each of your guesses has to have 5 letters as well")
print("After each guess, the program will tell you your progress. Out of the letters you entered, it will print:")
print("1) Capital letters of those that are in the word and in the correct spot") 
print("2) Lowercase letters of those are in the word but in the wrong spot")
print("3) Asterisks (*) for ones that are not in the word ") 

guess = input("Enter your first guess: ")
num_of_guesses = 0

def split(word_choice):
  return [char for char in word_choice] #splits the characters in the word into a list

word = split(word)

while num_of_guesses < 6:
  guess = split(guess)
  while len(guess) != 5: #checks that the user's guess is five letters
    print("Your guess must be a five letter word")
    guess = input("Enter another guess: ")
  result = "" 
  is_in_word = False 
  for i in range(0,5): #loops through each element/letter in the list
    if guess[i] == word[i]: #checks if that element in the user's guess matches the element in the same position in the correct word
      result = result + guess[i].upper() #adds that letter in uppercase to the "result" list
      is_in_word = True
    elif guess[i] in word and is_in_word == False: #checks if the element in guess is in the word and hasn't already been found in the correct place
      result = result + guess[i].lower() #adds it to the result in lowercase
      is_in_word = True
    else:
      result = result + "*"
  print(result) 
  num_of_guesses += 1 #adds one to the number of guesses
  if guess == word: #breaks out of the while loop if they guess the correct word
    print("Success!")
    if num_of_guesses == 1:
      print("It took you " + str(num_of_guesses) + " guess")
    else:
      print("It took you " + str(num_of_guesses) + " guesses") 
    break 
  guess = input("Enter your next guess: ")

if num_of_guesses >= 6:
  str = ""
  print("Your out of guesses! The word was: " + str.join(word) + ". Better luck next time!")
 

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
