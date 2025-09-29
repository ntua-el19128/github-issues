# github-issues

A FastAPI-based web application for GitHub issues management. This project provides a REST API interface for programmatic access to GitHub issues functionality.

## Project Description

The github-issues application is built with FastAPI, a modern Python web framework, designed to offer high-performance asynchronous capabilities for managing GitHub issues. The application serves as a foundation for building comprehensive GitHub issues management features through a clean REST API.

### Purpose and Goals

- Provide programmatic access to GitHub issues functionality
- Offer a REST API interface for developers and applications
- Enable efficient issue tracking and management workflows
- Serve as a scalable backend service for GitHub integration

### Current Status

The project is currently in its initial development phase with a basic API structure in place. The application includes a foundational endpoint that demonstrates the FastAPI framework setup and serves as a starting point for future GitHub issues management features.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Required Dependencies

The application requires the following Python packages:

- **fastapi**: Modern web framework for building APIs with Python
- **uvicorn**: Lightning-fast ASGI server implementation

### Installing Dependencies

To install all required dependencies, run:

```bash
pip install -r requirements.txt
```

This will install both fastapi and uvicorn as specified in the requirements.txt file.

## Setup Instructions

### Environment Setup

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/ntua-el19128/github-issues.git
   cd github-issues
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Currently, the application requires no additional configuration. Future versions may include environment variables for GitHub API authentication and other settings.

## Usage

### Running the Application

To start the development server with auto-reload enabled:

```bash
uvicorn app.main:app --reload
```

The application will start on `http://127.0.0.1:8000` by default.

### Command Options

- `--reload`: Enable auto-reload for development (watches for file changes)
- `--host 0.0.0.0`: Make the server externally accessible
- `--port 8080`: Change the port number

Example with custom host and port:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

### Accessing the API

Once the server is running, you can access the API at:

- **Base URL**: `http://127.0.0.1:8000`
- **Interactive API docs**: `http://127.0.0.1:8000/docs` (Swagger UI)
- **Alternative API docs**: `http://127.0.0.1:8000/redoc` (ReDoc)

## API Endpoints

### Current Endpoints

#### GET /

**Description**: Root endpoint that returns a welcome message

**Response**:
```json
{
  "message": "Hello, World!"
}
```

**Example**:
```bash
curl http://127.0.0.1:8000/
```

### Planned Functionality

The application is intended to provide the following GitHub issues management features:

- **List Issues**: Retrieve a list of issues from a repository
- **Get Issue Details**: Fetch detailed information about a specific issue
- **Create Issue**: Create new issues with title, body, and labels
- **Update Issue**: Modify existing issues (status, labels, assignees)
- **Search Issues**: Search and filter issues by various criteria
- **Comment Management**: Add, update, and delete comments on issues
- **Label Management**: Manage issue labels and assignments

These features will be implemented in future iterations of the project.

## Development

### Project Structure

```
github-issues/
├── src/
│   └── main.py          # Main FastAPI application entry point
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

### Future Enhancements

- GitHub API integration for real issue management
- Authentication and authorization mechanisms
- Database integration for caching and persistence
- Rate limiting and error handling
- Comprehensive test suite
- Deployment configurations

## License

This project is open source and available for educational and development purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
