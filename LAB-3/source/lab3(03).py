from tokenize import tokenize

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize
from nltk.util import ngrams
from collections import Counter, defaultdict

input="input.txt"
file = open('input.txt', 'r')
i= file.read()
tiles=[]
inp=i.split(" ")
lem = WordNetLemmatizer()
for word in inp:
     tiles.append(lem.lemmatize(word,"n"))  #lemmatization applied here
print(tiles)

data = sent_tokenize(i)
tiles1 = []
for words in data:
    tiles1.append(word_tokenize(words))   #Word tokenization applied here on sentences which were tokenized above.
print("Printing Tokenization")
print(tiles1)

words = nltk.word_tokenize(i)
bigram = ngrams(words,2)
print("Printing bigrams")
print(Counter(bigram))

count = defaultdict(int)
for n in ngrams(words, 2, False):
    count[n]=count[n]+1

print("Frequencies:")
for c, n in sorted(((c, n) for n, c in count.items()), reverse=True):
    print(c, n)

a = 0
b = 0
s = []

for line in i.splitlines():
    for a in range(5):

        if count[a] in line.split() and count[a] in line.split():
            # print("1")
            d = line.split().index(count[a])
            s.append(d)

print(s)
