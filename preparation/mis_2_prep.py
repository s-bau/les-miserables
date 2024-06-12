from .mis_1_cleaning import miserables_full


# pip install --upgrade spacy
# pip install --upgrade pydantic
# python -m spacy download fr_core_news_sm
import spacy

# Load the French language model in SpaCy
nlp = spacy.load('fr_core_news_sm')

from spacy.lang.fr.stop_words import STOP_WORDS

# Use SpaCy's stopwords for French
stopwords_fr = set(STOP_WORDS)

# Split the text into smaller chunks
chunk_size = 1000000
text_chunks = [miserables_full[i:i+chunk_size] for i in range(0, len(miserables_full), chunk_size)]

# Process each chunk separately
miserables_nostop_parts = []

for chunk in text_chunks:
    # tokenizing with spacy to get better results for French (e.g. "c'est" into "c'" and "est")
    doc = nlp(chunk.lower())

    # Filter out stopwords from the SpaCy tokens, tokens with length under 3, and those that start with "-"
    miserables_nostop_parts.append(" ".join([token.text for token in doc\
                                             if token.text not in stopwords_fr\
                                             and (len(token.text) > 2 and token.text[0] != "-")]))

# save full text as string without stop words in a variable
miserables_nostop = " ".join(miserables_nostop_parts)

# tokenize
miserables_tokens = miserables_nostop.split()

# enlever les noms et prénoms
# création d'une liste de personnages courantes avec chatgpt
noms_prenoms = [
    "Jean", "Valjean",
    "Cosette", "Thenardier",
    "Fantine", "Thénardier",
    "Marius", "Pontmercy",
    "Javert",
    "Eponine", "Thenardier",
    "Gavroche", "Thenardier",
    "Monsieur", "Thenardier",
    "Madame", "Thenardier",
    "Enjolras", "Pontmercy",
    "Monseigneur", "Bienvenu",
    "Azelma", "Thenardier",
    "Courfeyrac",
    "Feuilly",
    "Bahorel",
    "Jean", "Prouvaire",
    "Grantaire",
    "Mabeuf",
    "Fauchelevent",
    "Cosette", "Marius",
    "Georges", "Pontmercy",
    "Gillenormand", "Pontmercy",
    "Cosette", "Pontmercy",
    "Enjolras",
    "Monseigneur", "Myriel",
    "Charles", "Myriel",
    "Bienvenu", "Myriel"
]

noms_prenoms_lower = [name.lower() for name in noms_prenoms]

# save text as a string without names in a variable
miserables_nonames = ""

for word in miserables_tokens:
    if word not in noms_prenoms_lower:
        miserables_nonames += " " + word

# tokenize
miserables_nonames_tokens = miserables_nonames.split()