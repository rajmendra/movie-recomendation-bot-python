import random
from fuzzywuzzy import process

favorite_genres = []
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
    "comedy": ["The Hangover", "Superbad", "The Mask"],
    "horror": ["The Conjuring", "Get Out", "Hereditary"],
    "romance": ["The Notebook", "La La Land", "Titanic"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

print("🎬 Welcome to the Movie Recommendation Bot!")
print("Type 'exit' anytime to quit.\n")


while True:
    genre = input("What type of movie would you like to watch? (action, comedy, horror, romance, sci-fi): ").lower()

    if genre == "exit":
        print("\nThanks for using the Movie Bot! Goodbye! 👋")
        break

    # Use fuzzy matching here
    matched_genre, score = process.extractOne(genre, movies.keys())

    if score >= 60:  # If similarity is good enough
        recommended_movie = random.choice(movies[matched_genre])
        print(f"\n🎥 I recommend you watch: {recommended_movie} ({matched_genre.capitalize()} genre)\n")
        
        # Save the genre the user liked
        favorite_genres.append(matched_genre)

            # 🔥 ADD THE PERSONALIZATION CODE RIGHT HERE 🔥
        if len(favorite_genres) % 3 == 0 and len(favorite_genres) > 0:
            from collections import Counter
            genre_counter = Counter(favorite_genres)
            favorite_genre = genre_counter.most_common(1)[0][0]

            recommended_movie = random.choice(movies[favorite_genre])
            print(f"\n💬 Based on your favorites, you might love this {favorite_genre.capitalize()} movie: {recommended_movie}\n")


         # Ask if user wants another recommendation
        another = input("\nWould you like another recommendation? (yes/no): ").lower()
        if another != "yes":
            print("\nThanks for using the Movie Bot! Goodbye! 👋")
            break
        

    else:
        print("\n⚠️ Sorry, I don't have any recommendations for that genre.\n")


        
