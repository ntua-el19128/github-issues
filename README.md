# github-issues

## Project Description

The github-issues project is a FastAPI-based web service designed for GitHub issues management. This application provides a REST API for programmatic access to GitHub issues functionality. Currently, the project contains a foundational FastAPI application with a basic endpoint that can be extended with comprehensive GitHub issues management capabilities.

## Installation

To install the required dependencies, follow these steps:

1. Ensure you have Python 3.7 or higher installed on your system

2. Clone the repository:
   ```bash
   git clone https://github.com/ntua-el19128/github-issues.git
   cd github-issues
   ```

3. Install the dependencies from requirements.txt using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the FastAPI server, run the following command from the project root directory:

```bash
uvicorn src.main:app --reload
```

The `--reload` flag enables auto-reload mode, which automatically restarts the server when code changes are detected. This is useful for development.

Once the server is running, you can access:
- The API at: http://localhost:8000
- The interactive API documentation (Swagger UI) at: http://localhost:8000/docs
- The alternative API documentation (ReDoc) at: http://localhost:8000/redoc
