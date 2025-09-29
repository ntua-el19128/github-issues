# github-issues

A FastAPI-based REST API service for GitHub issues management.

## Project Description

This project provides a programmatic interface for managing GitHub issues through a clean REST API. Built with FastAPI and uvicorn, it offers high-performance asynchronous capabilities for interacting with GitHub issues data.

**Purpose**: Enable developers and applications to interact with GitHub issues functionality through a well-documented REST API, making it easier to automate issue tracking, reporting, and management workflows.

## Requirements

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ntua-el19128/github-issues.git
cd github-issues
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- `fastapi` - Modern web framework for building APIs
- `uvicorn` - ASGI web server for running the application

## Usage

### Running the Server

Start the FastAPI development server with auto-reload enabled:

```bash
uvicorn src.main:app --reload
```

The server will start at `http://localhost:8000`

### Example API Calls

Once the server is running, you can test the endpoints:

**Root Endpoint (Health Check)**
```bash
curl http://localhost:8000/
```

Response:
```json
{
  "message": "Hello, World!"
}
```

## API Documentation

### Available Endpoints

#### GET `/`
- **Description**: Root endpoint that returns a greeting message (health check)
- **Method**: GET
- **Response**: JSON object with a message field
- **Example Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: Navigate to `http://localhost:8000/docs` after starting the server
- **ReDoc**: Navigate to `http://localhost:8000/redoc` for alternative documentation

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is open source and available under the [MIT License](LICENSE).

## Development Status

This project is currently in early development. The API is being actively developed and additional endpoints for GitHub issues management will be added in future releases.

## Contact

For questions or issues, please open an issue on the GitHub repository.
