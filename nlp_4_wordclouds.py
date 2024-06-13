from preparation.mis_2_prep import miserables_nostop
from preparation.mis_2_prep import miserables_nonames

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# pip install wordcloud
from wordcloud import WordCloud

# Read the mask image
mask = np.array(Image.open("images/mask.png"))

# alternative
wordcloud = WordCloud(width=480,
                      height=480,
                      max_font_size=200,
                      min_font_size=10,
                      background_color='#e8ccbd',
                      colormap="copper",
                      mask=mask)

# Affichage grâce à Matplotlib
plt.figure(figsize=(12,6), facecolor="#e8ccbd")

plt.subplot(121)
wordcloud.generate_from_text(miserables_nostop)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)

plt.subplot(122)
wordcloud.generate_from_text(miserables_nonames)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)

plt.show()