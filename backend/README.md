
# 🌐 URL Shortening Service

A simple and efficient service to shorten long URLs into concise, shareable links.

---

## 📖 Overview

This project is solution of the **URL Shortening Service project from roadmap.sh (https://roadmap.sh/projects/url-shortening-service)**. It provides a platform for users to generate shortened URLs that redirect to the original addresses. The service offers a RESTful API enabling seamless integration and management of shortened links, including CRUD operations and access tracking.

---

## ✨ Features

- 🔗 **URL Shortening**: Convert lengthy URLs into short, easy-to-share links.
- 🔄 **Redirection**: Navigate users from the shortened URL to the original destination.
- 📝 **CRUD Operations**: Create, read, update, and delete shortened URLs.
- 📈 **Access Tracking**: Monitor the number of times each shortened URL is accessed.

[//]: # (- 🆔 **Custom Aliases**: Allow users to define custom short codes for their URLs.)

[//]: # (- ⏳ **Expiration Handling**: Set expiration times for shortened URLs to manage their validity.)

---

## 🛠️ Technology Stack

[//]: # (- **Caching**: Redis)

[//]: # (- **Task Queue**: Celery)

[//]: # (- **Containerization**: Docker)
- **Backend**: Python with FastAPI
- **Database**: PostgreSQL
- **Testing**: PyTest
- **Documentation**: Swagger UI

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13**

- **PostgreSQL**

- **Docker & Docker Compose**
- **Redis**

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HyTacker20/url-shortening-service.git
   cd url-shortening-service
   ```

2. **Set up a virtual environment**:
   ```bash
   pip install poetry
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   poetry shell
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```
   TESTING=True
   
   POSTGRES_USER=db_user
   POSTGRES_PASSWORD=db_password
   POSTGRES_NAME=db_name
   POSTGRES_HOST=db_host
   POSTGRES_PORT=db_port
   ```

5. **Create and apply database migrations**:
   ```bash
   alembic revision --autogenerate
   alembic upgrade head
   ```

6. **Start the application**:
   ```bash
   uvicorn main:app --reload
   ```

The service will be accessible at [http://localhost:8000](http://localhost:8000).

---

## 🐳 Docker Deployment


1. **Build and run the containers**:

   ```bash

   docker-compose up --build

   ```


The application will be available at [http://localhost:8000](http://localhost:8000).

---

## 📋 API Documentation

Interactive API documentation is available via Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs).

### Endpoints

- **Shorten URL**: `POST /shorten/`
- **Retrieve Original URL**: `GET /{short_code}/`
- **Update URL**: `PUT /{short_code}/`
- **Delete URL**: `DELETE /{short_code}/`
- **Access Statistics**: `GET /{short_code}/stats/`

---

## 🧪 Running Tests

Execute unit tests using PyTest:
```bash
pytest
```

---

## 🗺️ Project Roadmap

- [x] Implement caching
- [ ] Implement custom short code creation
- [ ] Implement comprehensive logging.
- [ ] Add exception handling mechanisms.
- [ ] Develop a user-friendly frontend interface.
- [ ] Integrate user authentication and authorization.
- [ ] Enhance analytics with detailed access statistics.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For inquiries, please contact [hermak20102004@gmail.com](mailto:hermak20102004@gmail.com).
