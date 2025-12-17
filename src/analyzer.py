from typing import List, Any
from src.models import Movie


def _get_top_certified_from_objects(movies: List[Movie], limit: int = 10) -> List[Movie]:
    """
    Internal function that operates on clean objects.
    Separates business logic from raw data structure.
    """
    fresh_movies = [m for m in movies if m.certified_fresh]
    sorted_movies = sorted(fresh_movies, key=lambda m: m.rating, reverse=True)
    return sorted_movies[:limit]


def analyze_movie_list(movie_list: List[List[Any]]) -> List[Movie]:
    """
    Takes the raw 'movie_list', performs internal refactoring
    and returns the top 10 certified movies.
    """

    # 1. Refactoring (Data Ingestion)
    # Convert raw data to our readable structure (Movie Class)
    # If there are corrupted rows, here is where we handle them.
    clean_movies = []
    for row in movie_list:
        try:
            movie = Movie.from_raw_list(row)
            clean_movies.append(movie)
        except (ValueError, IndexError):
            # In production, here we would log the error
            continue

    # 2. Business Logic
    return _get_top_certified_from_objects(clean_movies)
