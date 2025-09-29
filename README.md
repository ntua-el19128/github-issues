# github-issues

A FastAPI application for managing GitHub issues.

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## Testing

Run the test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=src
```
