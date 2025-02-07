# This program is for guessing letters.
# The program generate a word and guess number is equal to length
#pip -intall wonderwords

import wonderwords

from wonderwords import RandomWord
r = RandomWord()

#setting the minimum and maximum length
random_word = r.word(word_min_length=4,word_max_length=8)
print(random_word)

guess = len(random_word)
print(f' you have {guess} guess available')


correct_guess  = 0
wrong_guess   = 0

guessed_word = set()

while guess != 0:
    
    guessed_character = input("Please enter a character").lower()
        
    if guessed_character in random_word:
            guessed_word.add(guessed_character)
            correct_guess +=1
    else:
        wrong_guess +=1
        
    guess -=1


print (f'correct guesses {correct_guess}')
print (f'wrong guess {wrong_guess}')
print (f'guessed word {guessed_word}')
            