#word guessing game
import random
print("Welcome to the Word Guessing Game!")

words = ["home", "school", "python", "code", "computer", "game", "projects"]
word = random.choice(words)
guessWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
  print ("\nCurrent word: " + " ".join(guessWord) )
  guess = input("Pick a letter: ").lower()

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessWord[i] = guess
        print ("Great guess!")
  else:
    attempts -= 1
    print ("Try again! Attempts left: " + str(attempts))
  if '_' not in guessWord:
      print("\nYay! You guessed the word: " + word)
      break
else:
    print("You have run out of attempts. The word was: " + word)