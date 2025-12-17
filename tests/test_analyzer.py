import unittest
from src.analyzer import analyze_movie_list


class TestRawInputAnalyzer(unittest.TestCase):

    def test_analyzes_raw_list_correctly(self):
        # Raw input (list of lists)
        raw_input = [
            [1, 9.5, "Winner", True],
            [2, 2.0, "Loser", True],
            [3, 8.0, "Not Fresh", False]
        ]

        # Execute main function
        results = analyze_movie_list(raw_input)

        # Aserciones
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].title, "Winner")
        self.assertEqual(results[0].rating, 9.5)

    def test_handles_malformed_data(self):
        # Input with incomplete data
        bad_input = [
            [1, 9.5, "Good", True],
            ["This is not a movie"],
            [2, 8.0, "Okay", True]
        ]

        results = analyze_movie_list(bad_input)

        # Should ignore the bad row and process the rest
        self.assertEqual(len(results), 2)
