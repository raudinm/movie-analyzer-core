# Movie Analyzer Core

A Python utility designed to ingest raw movie data, refactor it into object-oriented structures, and calculate recommendations based on the "Certified Fresh" certification and rating.

## Installation and Execution

This project uses **Python 3.7+**. It does not require mandatory external dependencies for its basic execution.

### Run the script

```bash
python -m src.main
```

## 🧪 Testing

The test suite uses `unittest` to verify the functionality of the `analyze_movie_list` function. The tests ensure the system correctly processes raw data and handles edge cases.

### Running Tests

You can run the tests using the following command:

```bash
python -m unittest discover tests
```

### Test Coverage

The current test suite (`tests/test_analyzer.py`) includes:

- **Raw Input Analysis** (`test_analyzes_raw_list_correctly`):

  - Verifies that the function correctly ingests a list of lists (raw data).
  - Checks if the data is correctly converted into `Movie` objects.
  - Ensures the output is filtered and sorted correctly (Certified Fresh movies).

- **Malformed Data Handling** (`test_handles_malformed_data`):
  - Ensures that the function robustly handles and ignores rows with incomplete or incorrect data.
  - Verifies that the process continues without crashing when encountering bad data.

## 🐳 Development Environment (DevContainer)

This project includes an optional isolated execution environment using Docker Dev Containers. This setup provides a consistent, isolated development environment without affecting your host system.

### Setup Details

The Dev Container is configured with:

- Base image: Python 3.7-slim
- Installs: git, curl, build-essential

### Usage

To use the Dev Container:

1. Ensure you have Docker installed.
2. Ensure you have VS Code installed with the "Dev Containers" extension.
3. Open the project in VS Code.
4. When prompted, click "Reopen in Container" or use the Command Palette: `Dev Containers: Reopen in Container`.

This will build and open the project in an isolated Docker container, providing a consistent environment for development and testing.
