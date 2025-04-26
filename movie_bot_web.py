import random
import streamlit as st

# Movie database
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
    "comedy": ["The Hangover", "Superbad", "The Mask"],
    "horror": ["The Conjuring", "Get Out", "Hereditary"],
    "romance": ["The Notebook", "La La Land", "Titanic"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

# Streamlit app
st.title("🎬 Movie Recommendation Bot")

st.write("Choose a genre and I'll recommend a movie!")

# Dropdown menu
genre = st.selectbox(
    "Choose a genre:",
    options=["Select one", "Action", "Comedy", "Horror", "Romance", "Sci-Fi"]
)

# Recommend movie
if genre and genre != "Select one":
    recommended_movie = random.choice(movies[genre.lower()])
    st.subheader(f"🎥 I recommend you watch: {recommended_movie} ({genre} genre)")
