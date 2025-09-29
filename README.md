# github-issues

A FastAPI-based GitHub issues management service providing programmatic access to GitHub issues functionality through a REST API.

## Overview

This project is designed to provide a simple and efficient way to manage GitHub issues through a RESTful API. Built with FastAPI, it offers high performance and automatic API documentation. Currently in its initial development phase, the service provides a foundation for building comprehensive GitHub issues management capabilities.

## Features

- FastAPI-based REST API
- Automatic interactive API documentation (Swagger UI)
- High performance with async support
- Easy to extend and customize

## Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)

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

The project requires the following packages:
- `fastapi` - Modern web framework for building APIs
- `uvicorn` - ASGI server for running the application

## Usage

### Running the Application

Start the development server with auto-reload enabled:

```bash
uvicorn src.main:app --reload
```

The application will be available at `http://localhost:8000`

### API Endpoints

#### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Health check endpoint that returns a greeting message
- **Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### Interactive API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Development

### Project Structure

```
github-issues/
├── src/
│   └── main.py          # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Code Structure

- `src/main.py`: Contains the FastAPI application instance and route handlers
- The main application object is created with `app = FastAPI()`
- Route handlers are defined using decorators like `@app.get("/")`

### Adding New Endpoints

To add a new endpoint, define a new function in `src/main.py` with the appropriate decorator:

```python
@app.get("/new-endpoint")
def new_endpoint():
    return {"message": "New endpoint"}
```

FastAPI will automatically:
- Generate OpenAPI documentation
- Validate request/response data
- Serialize responses to JSON

### Testing

Testing procedures will be added as the project grows. Consider adding:
- Unit tests for individual endpoints
- Integration tests for API workflows
- Test coverage reporting

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and structure.

## License

This project is open source. License details to be determined.

## Contact & Support

- Repository: [github-issues](https://github.com/ntua-el19128/github-issues)
- Issues: [GitHub Issues](https://github.com/ntua-el19128/github-issues/issues)
- Maintainer: [@ntua-el19128](https://github.com/ntua-el19128)

For questions or support, please open an issue on GitHub.
