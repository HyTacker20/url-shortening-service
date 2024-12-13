
# 🌐 URL Shortening Service

A simple and efficient service to shorten long URLs into concise, shareable links.

---

## 📖 Overview

This project provides a platform for users to generate shortened URLs that redirect to the original addresses. It offers a RESTful API enabling seamless integration and management of shortened links, including CRUD operations and access tracking.

---

## ✨ Features

- 🔗 **URL Shortening**: Convert lengthy URLs into short, easy-to-share links.
- 🔄 **Redirection**: Navigate users from the shortened URL to the original destination.
- 📝 **CRUD Operations**: Create, read, update, and delete shortened URLs.
- 📈 **Access Tracking**: Monitor the number of times each shortened URL is accessed.
- ~~🆔 **Custom Aliases**: Allow users to define custom short codes for their URLs.~~ _in progress..._
- ~~⏳ **Expiration Handling**: Set expiration times for shortened URLs to manage their validity.~~ _in progress..._

---

## 🛠️ Technology Stack

- **Backend**: Python with FastAPI
- **Database**: PostgreSQL
- **Caching**: Redis
- **Task Queue**: Celery
- **Containerization**: Docker
- **Version Control**: Git
- **Testing**: PyTest
- **Documentation**: Swagger UI

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Docker & Docker Compose**
- **PostgreSQL**
- **Redis**

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/url-shortening-service.git
   cd url-shortening-service
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```
   DATABASE_URL=postgresql://postgres:password@localhost:5432/url_shortening
   REDIS_URL=redis://localhost:6379/0
   SECRET_KEY=your_secret_key
   ```

5. **Apply database migrations**:
   ```bash
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

For inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
