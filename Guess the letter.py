# This program is for guessing letters.
# The program generate a word and guess number is equal to length

import wonderwords

from wonderwords import RandomWord
r = RandomWord()
random_word = r.word(word_min_length=4,word_max_length=8)
print(random_word)

guess = len(random_word)
print(f' you have {guess} guess available')