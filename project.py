import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag

text =raw_input("Enter the sentence: ")


words=word_tokenize(text)
print (nltk.pos_tag(words))
