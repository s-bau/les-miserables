from preparation.mis_2_prep import miserables_nostop
from preparation.mis_2_prep import miserables_nonames

import matplotlib.pyplot as plt
# pip install wordcloud
from wordcloud import WordCloud

wordcloud = WordCloud(width=480, height=480, max_font_size=200, min_font_size=10)

# Affichage grâce à Matplotlib
plt.figure(figsize=(12,6))

plt.subplot(121)
wordcloud.generate_from_text(miserables_nostop)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title("Wordcloud avec noms et prénoms")

plt.subplot(122)
wordcloud.generate_from_text(miserables_nonames)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title("Wordcloud sans noms et prénoms")

plt.show()