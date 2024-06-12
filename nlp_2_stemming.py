from preparation.mis_2_prep import miserables_nostop
from preparation.mis_2_prep import miserables_tokens
from preparation.mis_2_prep import miserables_nonames
from preparation.mis_2_prep import miserables_nonames_tokens

import matplotlib.pyplot as plt
import nltk
nltk.download("popular")
from nltk.stem import SnowballStemmer


miserables_stem = ""
stem_fr = SnowballStemmer("french")
for word in miserables_tokens:
        miserables_stem += " " + stem_fr.stem(word)

miserables_stem_nonames = ""
stem_fr = SnowballStemmer("french")
for word in miserables_nonames_tokens:
        miserables_stem_nonames += " " + stem_fr.stem(word)

# counting the frequency of all words
freq_stem = nltk.FreqDist(miserables_stem.split(" "))

# turning the frequency into a list of tuples
freq_stem = sorted(zip(freq_stem.values(), freq_stem.keys()), reverse=True)

# keeping only the top words in a new dictionary
top_stem = dict()
for i in range(15):
    top_stem[freq_stem[i][1]] = freq_stem[i][0]


# without names
freq_stem_nonames = nltk.FreqDist(miserables_stem_nonames.split(" "))

# turning the frequency into a list of tuples
freq_stem_nonames = sorted(zip(freq_stem_nonames.values(), freq_stem_nonames.keys()), reverse=True)

# keeping only the top words in a new dictionary
top_stem_nonames = dict()
for i in range(15):
    top_stem_nonames[freq_stem_nonames[i][1]] = freq_stem_nonames[i][0]


# Plotting
plt.figure(figsize = (20,12))

plt.subplot(211)
plt.bar(top_stem.keys(), top_stem.values())
plt.title("Stemmatizing : Les mots les plus utilisés par Victor Hugo (sans stopwords)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45)

plt.subplot(212)
plt.bar(top_stem_nonames.keys(), top_stem_nonames.values())
plt.title("Stemmatizing : Les mots les plus utilisés par Victor Hugo (sans stopwords et sans noms/prénoms)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()