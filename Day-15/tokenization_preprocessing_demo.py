# Day 15: Tokenization & Preprocessing Demo
# This script demonstrates basic tokenization and preprocessing steps on sample text

import matplotlib.pyplot as plt
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')

# Sample text
text = "Tokenization and preprocessing are essential for preparing text data in AI. This process includes cleaning, splitting, and normalizing text."

# Lowercase and remove punctuation
text_clean = re.sub(r'[^\w\s]', '', text.lower())

# Tokenize
tokens = text_clean.split()

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens_nostop = [t for t in tokens if t not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(t) for t in tokens_nostop]

# Visualize token distribution
plt.figure(figsize=(8, 4))
plt.bar(Counter(stemmed_tokens).keys(), Counter(stemmed_tokens).values())
plt.title('Token Distribution After Preprocessing')
plt.xlabel('Token')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Day-15/tokenization_preprocessing_results.png')
