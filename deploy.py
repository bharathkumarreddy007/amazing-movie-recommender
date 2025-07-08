# Amazing Movie Recommender
# Customized and deployed by A.V. Bharath Kumar Reddy

import streamlit as st
import pandas as pd
import pickle
import requests

# ✅ Load API key securely from Streamlit Secrets
API_KEY = st.secrets["API_KEY"]

# Fetch movie poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    except Exception as e:
        print(f"Error fetching poster: {e}")
    return None

# Recommendation logic
def recommendation(title, data):
    normalized_title = title.strip().lower()
    data['normalized_title'] = data['TITLE'].str.strip().str.lower()

    if normalized_title not in data['normalized_title'].values:
        return []

    movie_index = data[data['normalized_title'] == normalized_title].index[0]
    distances = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[:10]

    recommended_movies = []
    for i in movies_list:
        movie_id = data.iloc[i[0]].FILMID
        movie_title = data.iloc[i[0]].TITLE
        poster_url = fetch_poster(movie_id)
        recommended_movies.append((movie_title, poster_url))

    return recommended_movies

# Load data
data = pd.read_csv('data.csv')
with open("similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Amazing Movie Recommender", layout="wide")
st.title('🍿 Amazing Movie Recommender')

selected_movie = st.selectbox(
    '🎬 Select a movie to get personalized recommendations:',
    data['TITLE'].values
)

if st.button('Recommend'):
    with st.spinner('🔍 Finding your next favorites...'):
        results = recommendation(selected_movie, data)

        if not results:
            st.error("⚠️ Movie not found in database. Try another?")
        else:
            cols = st.columns(5)
            for idx, (name, poster) in enumerate(results):
                with cols[idx % 5]:
                    if poster:
                        st.image(poster, use_container_width=True)
                    st.caption(name)

st.markdown("**🔧 Customized and deployed by Bharath Reddy – for portfolio use.**")
st.info("✅ Uses TMDB API and cosine similarity to generate real-time suggestions.")
