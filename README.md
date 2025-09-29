# github-issues

A FastAPI-based REST API for GitHub issues management. This project is currently in early development stage with minimal implementation.

## Description

The `github-issues` project aims to provide a comprehensive REST API for managing GitHub issues programmatically. Built with FastAPI for high performance and modern Python async capabilities, this service will enable developers and applications to interact with GitHub issues through a clean, well-documented API interface.

**Current Status:** Early development - basic FastAPI scaffold with health check endpoint  
**Future Vision:** Full-featured GitHub issues management API with complete CRUD operations

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Dependencies

This project uses the following dependencies (defined in `requirements.txt`):
- `fastapi` - Modern, fast web framework for building APIs
- `uvicorn` - Lightning-fast ASGI server implementation

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ntua-el19128/github-issues.git
cd github-issues
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Current API Endpoints

The following endpoints are currently implemented:

### Health Check
- **Endpoint:** `GET /`
- **Description:** Returns a simple greeting message to verify the API is running
- **Response:**
  ```json
  {
    "message": "Hello, World!"
  }
  ```
- **Status Code:** 200 OK

## Future/Planned API Endpoints

The following endpoints are planned for implementation:

### List Issues
- **Endpoint:** `GET /issues`
- **Description:** Retrieve a list of all GitHub issues
- **Status:** Not yet implemented

### Get Issue by ID
- **Endpoint:** `GET /issues/{id}`
- **Description:** Retrieve details of a specific issue by its ID
- **Status:** Not yet implemented

### Create Issue
- **Endpoint:** `POST /issues`
- **Description:** Create a new GitHub issue
- **Status:** Not yet implemented

### Update Issue
- **Endpoint:** `PATCH /issues/{id}`
- **Description:** Update an existing issue
- **Status:** Not yet implemented

### Delete Issue
- **Endpoint:** `DELETE /issues/{id}`
- **Description:** Delete a specific issue
- **Status:** Not yet implemented

## Usage

### Running the Development Server

Start the FastAPI development server with hot-reload enabled:

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### Accessing the API

Once the server is running, you can:

1. **Test the health check endpoint:**
   ```bash
   curl http://localhost:8000/
   ```

2. **View interactive API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

FastAPI automatically generates interactive API documentation that allows you to explore and test endpoints directly from your browser.

## Testing

### Current Status
Automated tests are not yet implemented for this project.

### Future Testing Approach
Testing will be implemented using `pytest` with the following structure:
- Unit tests for individual functions and endpoints
- Integration tests for API workflows
- Test coverage reports

### Manual Testing

To manually test the current endpoint:

```bash
# Start the server
uvicorn src.main:app --reload

# In another terminal, test the endpoint
curl http://localhost:8000/
# Expected output: {"message":"Hello, World!"}
```

## Development Setup

### Project Structure

```
github-issues/
├── src/
│   └── main.py          # Main FastAPI application entry point
├── requirements.txt     # Python package dependencies
└── README.md           # Project documentation (this file)
```

### Key Files

- **`src/main.py`**: Contains the FastAPI application instance and route handlers
- **`requirements.txt`**: Lists all Python dependencies required for the project

### Development Workflow

1. Make changes to the code
2. The development server will automatically reload (when using `--reload` flag)
3. Test your changes using the interactive docs at `/docs`
4. Run tests (once implemented)
5. Commit your changes following the contributing guidelines

## Contributing

We welcome contributions to the github-issues project! Here's how you can help:

### Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

### Branch Naming Conventions

Use descriptive branch names:
- Feature branches: `feature/description-of-feature`
- Bug fixes: `bugfix/description-of-bug`
- Documentation: `docs/description-of-change`

### Code Style and Conventions

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Write clean, readable code

### Pull Request Process

1. Update the README.md or documentation if needed
2. Ensure all tests pass (once testing is implemented)
3. Provide a clear description of your changes
4. Reference any related issues in your PR description
5. Wait for code review and address any feedback

### Questions or Issues?

If you have questions or encounter issues:
- Open an issue on GitHub with detailed information
- Check existing issues to see if your question has been answered
- Provide clear reproduction steps for bugs

## License

[Add license information here]

## Contact

For questions or support, please open an issue on GitHub.

---

**Note:** This project is under active development. Features and API endpoints are subject to change.
