from nltk import trigrams
from nltk import WhitespaceTokenizer
import random
import re

text = input()
with open(text, "r", encoding="utf-8") as GoT_Script:
    text = GoT_Script.read()
tk = WhitespaceTokenizer()
text1 = tk.tokenize(text)
tri_grams = list(trigrams(text1))

head_tail = {}
for tri_gram in tri_grams:
    head = tri_gram[0] + " " + tri_gram[1]
    tail = tri_gram[2]
    head_tail.setdefault(head, {})
    head_tail[head].setdefault(tail, 0)
    head_tail[head][tail] += 1

reg = re.compile("^[A-Z][a-z ]*[^.?!]$")
reText1 = list(filter(reg.match, head_tail.keys()))

sentence = []
for i in range(10):
    random_word = random.choice(reText1)
    prev_token = random_word
    while not (prev_token[-1] in ".?!" and len(sentence) >= 3):
        sentence.append(random_word)
        probable_tails = list(head_tail[prev_token].keys())
        weights = list(head_tail[prev_token].values())
        random_word = random.choices(probable_tails, weights)[0]
        prev_token = prev_token.split(" ")[1] + " " + random_word
    sentence.append(random_word)
    print(" ".join(sentence))
    sentence = []
