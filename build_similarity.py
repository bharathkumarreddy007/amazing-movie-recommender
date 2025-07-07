import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load your movie data
df = pd.read_csv('data.csv')

# Normalize titles
df['normalized_title'] = df['TITLE'].str.strip().str.lower()

# Use movie titles for now (you can improve this later by adding genres/descriptions)
combined = df['TITLE']

# Generate count vectors and compute cosine similarity
cv = CountVectorizer(tokenizer=lambda x: x.split())
matrix = cv.fit_transform(combined)
similarity = cosine_similarity(matrix)

# Save to a pickle file
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("✅ similarity.pkl generated successfully.")
