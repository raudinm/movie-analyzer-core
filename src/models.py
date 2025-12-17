from dataclasses import dataclass


@dataclass
class Movie:
    """
    Data Transfer Object that represents a movie.
    We use dataclasses to reduce boilerplate code.
    """
    id: int
    rating: float
    title: str
    certified_fresh: bool

    @classmethod
    def from_raw_list(cls, data: list):
        """Factory method to instantiate from the raw legacy list."""
        # Validación básica de estructura
        if len(data) < 4:
            raise ValueError(f"Incomplete data for the movie: {data}")

        return cls(
            id=int(data[0]),
            rating=float(data[1]),
            title=str(data[2]),
            certified_fresh=bool(data[3])
        )
