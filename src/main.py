from src.analyzer import analyze_movie_list

# Mock data
movie_list = [
    [1, 9.0, 'Interstellar', True],
    [2, 8.5, 'Fast and the Furious', True],
    [3, 7.8, 'Eternals', False],
    [4, 9.5, 'The Godfather', True],
    [5, 6.0, 'Gigli', False],
    [6, 8.9, 'Pulp Fiction', True],
    [7, 9.1, 'The Dark Knight', True],
    [8, 8.0, 'Avatar', True],
    [9, 8.7, 'Inception', True],
    [10, 7.5, 'Suicide Squad', False],
    [11, 9.3, 'Schindler\'s List', True],
    [12, 8.6, 'Forrest Gump', True],
    [13, 7.9, 'The Matrix', True],
    [14, 9.4, '12 Angry Men', True]
]


def main():
    print("\n------- Executing Movie Analyzer -------")

    top_picks = analyze_movie_list(movie_list)

    print(f"\n✅ Found {len(top_picks)} recommendations:")
    print("-" * 40)
    print(f"{'RATING':<8} | {'TITLE'}")
    print("-" * 40)

    for movie in top_picks:
        print(f"{movie.rating:<8} | {movie.title}")

    print("-" * 40)


if __name__ == "__main__":
    main()
