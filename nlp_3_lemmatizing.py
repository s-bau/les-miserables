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
for i in range(10):
    top_lem[freq_lem[i][1]] = freq_lem[i][0]


# nonames
freq_lem_nonames = nltk.FreqDist(miserables_lem_nonames.split(" "))
freq_lem_nonames = sorted(zip(freq_lem_nonames.values(), freq_lem_nonames.keys()), reverse=True)
top_lem_nonames = dict()
for i in range(10):
    top_lem_nonames[freq_lem_nonames[i][1]] = freq_lem_nonames[i][0]


# plotting
plt.figure(figsize = (20, 12), facecolor='#e8ccbd')

ax1 = plt.subplot(211, facecolor="#e8ccbd")
bars1 = plt.bar(top_lem.keys(), top_lem.values(), color='#8B0000', edgecolor="#e8ccbd")
plt.xticks(rotation=45, fontsize=20, fontweight="bold")
plt.yticks([])

# Adding tick labels inside the bars
for bar in bars1:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
             str(int(bar.get_height())), ha='center', va='bottom', fontsize=16, color="grey", fontweight="bold")

# Remove frame (spines) for ax1
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)


ax2 = plt.subplot(212, facecolor="#e8ccbd")
bars2 = plt.bar(top_lem_nonames.keys(), top_lem_nonames.values(), color='#CD5C5C')
plt.xticks(rotation=45, fontsize=20, fontweight="bold")
plt.yticks([])

for bar in bars2:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 1,
             str(int(bar.get_height())), ha='center', va='bottom', fontsize=16, color="grey", fontweight="bold")

# Remove frame (spines) for ax1
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()