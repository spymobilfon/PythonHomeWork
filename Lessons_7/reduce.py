from functools import reduce

def length_of_word(word):
    split_word = list(word)
    return reduce(lambda character, smth: character + 1, split_word, 0)

word_list = ['some', 'other', 'value']

for one_word in word_list:
    length = length_of_word(one_word)
    print("The length of word", one_word.upper(), "is", length)