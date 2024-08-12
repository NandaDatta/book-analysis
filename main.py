# import re is regular expression module
import re

# nltk is a python's Natural Language Toolkit
import nltk
# nltk.download('stopwords')
# nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# loading the book
with open("miracle_in_the_andes.txt", 'r', encoding="utf-8") as file:
    book = file.read()

# how many chapters are in the book?
# by using string methods
print(book.count("Chapter"))

# by using regular expression or regx
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)
print(findings)


# which are the sentences where love is used
pattern1 = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
find = re.findall(pattern1, book)
print(find)

pattern1 = re.compile("[^\n]+love[^\n]+")
find = re.findall(pattern1, book)
print(find)


# Getting the titles of the chapters / model-1
pattern1 = re.compile("[a-zA-Z, ]+\n\n")
find = re.findall(pattern1, book)
find = [item.strip("\n") for item in find]
print(find)

pattern1 = re.compile("([a-zA-Z ]+)\n\n")
find = re.findall(pattern1, book)
print(find)

# what are the most common words
pattern2 = re.compile("[a-zA-Z]+")
find1 = re.findall(pattern2, book.lower())
print(find1[:10])

d = {}
for word in find1:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]

print(sorted(d_list, reverse=True))

# most used words which are non articles
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
# findings[:10]

d = {}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
# print(d)

d_list = [(value, key) for (key, value) in d.items()]
d_list = (sorted(d_list, reverse=True))

english_stopwords = stopwords.words("english")

# most used words (non-article)
filtered_words = []

for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

# print(filtered_words)

# Sentiment Analysis: What is most positive and most negative chapter
analyzer = SentimentIntensityAnalyzer()

# chapter sentiment analysis

pattern1 = re.compile('Chapter [0-9]+')
chapters = re.split(pattern1, book)
chapters = chapters[1:]

for nr, chapter in enumerate(chapters):
    scores = analyzer.polarity_scores(chapter)
    if scores['pos'] > scores['neg']:
        print(f"Result:Chapter {nr+1} It is a positive text.")
    else:
        print(f"Result:Chapter {nr+1} It is a negative text.")
    print(f'Chapter {nr+1} {scores}')
