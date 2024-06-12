from preparation.mis_2_prep import miserables_nostop
from preparation.mis_2_prep import miserables_tokens
from preparation.mis_2_prep import miserables_nonames
from preparation.mis_2_prep import miserables_nonames_tokens
from preparation.mis_2_prep import nlp

import matplotlib.pyplot as plt
import nltk
nltk.download("popular")

# Split the text into smaller chunks
chunk_size = 1000000
text_chunks = [miserables_nostop[i:i+chunk_size] for i in range(0, len(miserables_nostop), chunk_size)]

# Process each chunk separately
miserables_lem = ""

for chunk in text_chunks:
    sent_tokens = nlp(chunk.lower())

    for token in sent_tokens:
        miserables_lem += " " + token.lemma_

# same without names
chunk_size = 1000000
text_chunks = [miserables_nonames[i:i+chunk_size] for i in range(0, len(miserables_nonames), chunk_size)]

miserables_lem_nonames = ""

for chunk in text_chunks:
    sent_tokens = nlp(chunk.lower())

    for token in sent_tokens:
        miserables_lem_nonames += " " + token.lemma_

# counting the frequency of all words
freq_lem = nltk.FreqDist(miserables_lem.split(" "))

# turning the frequency into a list of tuples
freq_lem = sorted(zip(freq_lem.values(), freq_lem.keys()), reverse=True)

# turning the top words into a dictionary
top_lem = dict()
for i in range(15):
    top_lem[freq_lem[i][1]] = freq_lem[i][0]


# nonames
freq_lem_nonames = nltk.FreqDist(miserables_lem_nonames.split(" "))
freq_lem_nonames = sorted(zip(freq_lem_nonames.values(), freq_lem_nonames.keys()), reverse=True)
top_lem_nonames = dict()
for i in range(15):
    top_lem_nonames[freq_lem_nonames[i][1]] = freq_lem_nonames[i][0]

# Plotting
plt.figure(figsize = (20,12))

plt.subplot(211)
plt.bar(top_lem.keys(), top_lem.values())
plt.title("Lemmatizing : Les mots les plus utilisés par Victor Hugo (sans stopwords)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45)

plt.subplot(212)
plt.bar(top_lem_nonames.keys(), top_lem_nonames.values())
plt.title("Lemmatizing : Les mots les plus utilisés par Victor Hugo (sans stopwords et sans noms/prénoms)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")

plt.tight_layout()
plt.show()