import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

text = """
this is my program about text analyze 
please enter:
    1 - for data management
    2 - for start the app
    3 - for end the app
"""
text1 = """
1 - for show the data
2 - for write new date
3 - for update the data
# """
# user_input = int(input(f'{text}\nyour reply: '))


def parsing(file):
    file = file.split()
    return file


def dead_words(tokens):

    file = open("deadwords.txt", "r")
    stop_WORD= file.read()
    list_of_dead_words = stop_WORD.split()
    file.close()
    for dead in list_of_dead_words:
        for word in tokens:
            if word == dead:
                tokens.remove(word)
            else:
                pass
    return tokens

def stemming(tokens):
    ps = PorterStemmer()
    stem = []
    for word in tokens:
        stem.append(ps.stem(word))
    return stem

file = open('data.txt', 'r')
tokens = parsing(file.read())
print(f"the first step (parsing):\n{tokens}\n")
file.close()
tokens_with_out_dead_end = dead_words(tokens)
print(f"the second step('removing the stop words):\n{tokens_with_out_dead_end}\n")
stem = stemming(tokens_with_out_dead_end)
print(f"the third step(stemming):\n{stem}\n")


sys.exit("the end...")

