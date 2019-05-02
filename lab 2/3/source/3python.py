import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

# Part a. Read the data from a file
with open('nlp_input.txt') as data:
    text = data.read().strip()


from string import punctuation
stoplist = set(list(punctuation))

# Punctuation was not wanted to be part of the tokens created
tokens = [token for token in nltk.word_tokenize(text) if token.lower() not in stoplist]

for i in tokens:
    print(i)

print()


""" lematization for each word"""
print("le----------------------------------------------------------")
#Lemmatize each word
lemmat = WordNetLemmatizer()

for l in tokens:
    print(lemmat.lemmatize(str(l)))

print()


#trigrms
trigrams = ngrams(tokens,3)
for i in trigrams:
    print(i)
print()


runs = 0
most_trigrams = ()
for t in trigrams2:
    most_trigrams = most_trigrams + (t,)
    runs += 1
    if runs >= 10:
        break

for g in most_trigrams:
    print(g)
print()


#top 10 trigrams
temp = nltk.collocations.TrigramCollocationFinder.from_words(tokens)

trigrams2 = sorted(temp.ngram_fd.items(), key=lambda t: (-t[1], t[0]))


runs = 0
most_trigrams = ()
for t in trigrams2:
    most_trigrams = most_trigrams + (t,)
    runs += 1
    if runs >= 10:
        break

for g in most_trigrams:
    print(g)
print()


#repeated trigrams and concatenate
stokens = nltk.sent_tokenize(text)
most_trigrams2 = ()
for i,u in most_trigrams:
    most_trigrams2 = most_trigrams2 + (i,)
tristrings = []
temporary = list(most_trigrams2)
for d in range(0,10):
    tempstring = ' '.join(temporary[d])
    tristrings.append(tempstring)
Sentlist = list(stokens)
Sentences = []
temps = []

for k in range(len(tristrings)):
    temps2 = ''
    temps = []
    for i in range(len(Sentlist)):
        # Check to see if trigram string is in the Sentence string
        if tristrings[k] in Sentlist[i]:
            # Append Sentences to a list
            temps.append(Sentlist[i])
    temps2 = ' '.join(temps)
    Sentences.append(temps2)

# Part h. Print the concatenated result
q = 1
for i in Sentences:
    print(q)
    print(i)
    print()
    q += 1



