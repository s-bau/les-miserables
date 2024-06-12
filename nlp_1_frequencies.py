from preparation.mis_2_prep import miserables_nostop
from preparation.mis_2_prep import miserables_tokens
from preparation.mis_2_prep import miserables_nonames
from preparation.mis_2_prep import miserables_nonames_tokens

import matplotlib.pyplot as plt


# Initialize an empty dictionary to store word frequencies
word_counts = {}

# Count word frequencies excluding stopwords and single characters and 2-character words
for word in miserables_tokens:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort the dictionary by value in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# without names
word_counts_nonames = {}

# Count word frequencies excluding stopwords and single characters and 2-character words
for word in miserables_nonames_tokens:
    if word in word_counts_nonames:
        word_counts_nonames[word] += 1
    else:
        word_counts_nonames[word] = 1

# Sort the dictionary by value in descending order
sorted_word_counts_nonames = sorted(word_counts_nonames.items(), key=lambda x: x[1], reverse=True)

# Get the top words
top_words = dict(sorted_word_counts[:15])
top_words_nonames = dict(sorted_word_counts_nonames[:15])

# Plotting
plt.figure(figsize = (20, 12))

plt.subplot(211)
plt.bar(top_words.keys(), top_words.values())
plt.title("Les mots les plus utilisés par Victor Hugo (sans stopwords)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45)

plt.subplot(212)
plt.bar(top_words_nonames.keys(), top_words_nonames.values())
plt.title("Les mots les plus utilisés par Victor Hugo (sans stopwords et sans noms/prénoms)")
plt.ylabel("Nombre d'occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()