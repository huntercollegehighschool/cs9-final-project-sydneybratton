"""
Name(s): Sydney Bratton and Logan Lee
Name of Project: WORDLE
"""
import random

max_guesses = 6
filename = "words.txt"
with open(filename) as file:
    listofwords = file.readlines()
    listofwords = [line.rstrip() for line in listofwords]

word = random.choice(listofwords) #picks a random word from the listofwords
word = word.upper()

print("Welcome to WORDLE 2.0\nHere, you will have " + str(max_guesses) + " tries to guess a 5 letter word, and each of your guesses has to have 5 letters as well. \nAfter each guess, the program will tell you your progress. Out of the letters you entered, it will print: \n1) Capital letters for those that are in the word and in the correct spot \n2) Lowercase letters for those in the word but in the wrong spot \n3) Asterisks (*) for letters that are not in the word \nTo make this a little easier none of the words have the same letter twice!")

guess = input("Enter your first guess: ")

num_of_guesses = 0

def split(word_choice):
  return [char for char in word_choice] #splits the characters in the word into a list

# word = split(word)

while num_of_guesses < max_guesses:
  # guess = split(guess)

  while ' ' in guess:
    print("Your guess cannot have spaces")
    guess = input("Enter another guess: ")

  while str.isalpha(guess) == False:
    print("That is not a word.")
    guess = input("Enter another guess: ")

  while len(guess) != 5: #checks that the user's guess is five letters
    print("Your guess must be a five letter word");
    guess = input("Enter another guess: ")
  
  guess = guess.upper()
  result = "" 
  
  for i in range(0,5): #loops through each element/letter in the list
    letter = guess[i]
    if letter == word[i]: #checks if that element in the user's guess matches the element in the same position in the correct word
      result = result + letter #adds that letter in uppercase to the "result" list
    elif letter in word: #checks if the element in guess is in the word and hasn't already been found in the correct place
      result = result + letter.lower() #adds it to the result in lowercase
    else:
      result = result + "*"

  print(result) 
  
  num_of_guesses += 1 #adds one to the number of guesses
  
  if num_of_guesses == 1:
    suffix = ""
  else:
    suffix = "es"

  if guess == word: #breaks out of the while loop if they guess the correct word
    print("Success!")
    print("It took you " + str(num_of_guesses) + " guess" + suffix)
    break 
  
  if num_of_guesses >= max_guesses:
    str = ""
    print("You're out of guesses! The word was " + str.join(word) + ". Better luck next time!")
    break

  num_of_guesses_left = max_guesses - num_of_guesses
  if num_of_guesses_left == 1:
    suffix = ""
  else:
    suffix = "es"
    
  print("You have " + str(num_of_guesses_left) + " guess" + suffix + " left.")

  guess = input("Enter your next guess: ")
  


 

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
