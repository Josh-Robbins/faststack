# FastStack

## Overview
FastStack is a web application built with FastAPI for managing items and users. It uses PostgreSQL as the database and includes Docker support for containerization.

## Features
- RESTful API for items and users
- JWT-based authentication
- Asynchronous database operations with SQLAlchemy
- Alembic for database migrations
- Docker support
- CI/CD with GitHub Actions

## Setup

### Prerequisites
- Docker
- Docker Compose
- Python 3.9+
- Node.js and npm

### Environment Variables
Create a `.env` file in the root directory with the following content:
- DATABASE_URL=postgresql+asyncpg://myuser:mypassword@localhost/mydatabase
- SECRET_KEY=your_secret_key
- ALGORITHM=HS256
- ACCESS_TOKEN_EXPIRE_MINUTES=30

### Running the Application

1. **Build and Run with Docker Compose**

```bash
docker-compose up --build
```

2. **Run Alembic Migrations**

```bash
docker-compose run --rm app alembic upgrade head
```

3. **Build Tailwind CSS**

```bash
npm install
npm run build:css
```

4. **Run the Tests**

```bash
docker-compose exec fastapi-app pytest
```

### Accessing the Application

- API Documentation: http://localhost:80/docs
- Home Page: http://localhost:80

### License
This project is licensed under the MIT License.
