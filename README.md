# Les Misérables

An analysis of Victor Hugo's *Les Misérables* using different natural language processing models

Data mission at Wild Code School (2 days)

* Data preparation (cleaning and tokenizing)
* NLP models to visualize the most frequent words (with and without character names)

<img src=images/nlp_4_wordclouds.jpg>

## Data preparation

The package **preparation** retrieves and cleans the full text of *Les Misérables* in its original French version from [gutenberg.org](https://gutenberg.org/ebooks/search/?query=victor+hugo&submit_search=Go%21). Everything that is not part of the main text is removed (such as the list of chapters) and the main text is comined in one single string of text. **mis_2_prep.py** removes all French stopwords and tokenizes the text using spaCy. It also creates a version of text/tokens that removes the last and first names of the most prominent characters.

## NLP

The nlp files visualize the most common words using different models, both with and without character names:
* frequency count of tokens
* frequency count of stemmed tokens
* frequency count of lemmatized tokens
* word cloud of token frequency

#### Top 10 words with and without character names
<img src=images/nlp_1_frequencies.jpg>

#### Top 10 words (excluding character names) using lemmatization
<img src=images/nlp_3_lemmatizing.jpg>
