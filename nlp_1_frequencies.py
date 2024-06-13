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
top_words = dict(sorted_word_counts[:10])
top_words_nonames = dict(sorted_word_counts_nonames[:10])

plt.figure(figsize = (20, 12), facecolor='#e8ccbd')

ax1 = plt.subplot(211, facecolor="#e8ccbd")
bars1 = plt.bar(top_words.keys(), top_words.values(), color='#8B0000', edgecolor="#e8ccbd")
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
bars2 = plt.bar(top_words_nonames.keys(), top_words_nonames.values(), color='#CD5C5C')
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