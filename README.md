# GitHub Issues Management API

A FastAPI-based web service for managing GitHub issues programmatically. This project provides a REST API interface for interacting with GitHub issues, built with modern Python web technologies.

## Purpose

This application is designed to provide developers and applications with programmatic access to GitHub issues functionality through a clean, fast REST API. Built with FastAPI for high performance and automatic API documentation generation.

## Installation

### Prerequisites
- Python 3.7+
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

The required dependencies are:
- `fastapi` - Modern, fast web framework for building APIs
- `uvicorn` - ASGI web server for running FastAPI applications

## API Endpoints

### Current Endpoints

#### GET /
Returns a simple greeting message to verify the API is running.

**Response:**
```json
{
  "message": "Hello, World!"
}
```

### Future Endpoints
This API will be extended with the following GitHub issues management endpoints:
- `GET /issues` - List GitHub issues
- `POST /issues` - Create new GitHub issue
- `GET /issues/{id}` - Get specific issue details
- `PUT /issues/{id}` - Update existing issue
- `DELETE /issues/{id}` - Delete issue

## Usage

### Running the Application Locally

Start the development server using uvicorn:

```bash
uvicorn src.main:app --reload
```

The API will be available at:
- **Application**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

### Testing the API

You can test the root endpoint using curl:

```bash
curl http://localhost:8000/
```

Expected response:
```json
{"message": "Hello, World!"}
```

## Development Setup

### Development Environment
1. Follow the installation steps above
2. Install additional development dependencies (if any are added in the future)
3. Run the application in development mode with auto-reload:
   ```bash
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Project Structure
```
github-issues/
├── src/
│   └── main.py          # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Contributing

We welcome contributions to improve the GitHub Issues Management API! Here's how you can contribute:

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes locally
5. Commit your changes: `git commit -m "Add your feature description"`
6. Push to your branch: `git push origin feature/your-feature-name`
7. Create a Pull Request

### Development Guidelines
- Follow Python PEP 8 style guidelines
- Write clear, descriptive commit messages
- Test your changes before submitting
- Update documentation as needed
- Ensure FastAPI best practices are followed

### Code Style
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Follow FastAPI patterns and conventions

## License

This project is open source. Please check the repository for license details.

## Support

For questions, issues, or contributions, please use the GitHub Issues tab in this repository.
