# 🚗 Car Price Prediction API

> **Production-ready Machine Learning inference API built with FastAPI, JWT Authentication, Redis Caching, Prometheus, Grafana, Docker, and CI/CD.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production%20API-009688.svg)](https://fastapi.tiangolo.com/)
[![Redis](https://img.shields.io/badge/Redis-Caching-red.svg)](https://redis.io/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange.svg)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800.svg)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF.svg)](https://github.com/features/actions)

---

## 📌 Overview

**Car Price Prediction API** is an end-to-end ML backend designed to demonstrate how a machine learning model can be transformed into a **secure, scalable, monitored, and production-ready API service**.

Instead of exposing a machine learning model through a simple Python script or notebook, this project wraps the complete prediction workflow inside a modern backend architecture.

The system includes:

* ⚡ High-performance **FastAPI** REST APIs
* 🔐 **JWT-based authentication**
* 🧩 Custom **middleware**
* 🤖 Machine Learning based car price prediction
* ⚡ **Redis caching** for faster repeated predictions
* 📊 **Prometheus metrics**
* 📈 **Grafana dashboards**
* 🧪 Automated testing with **Pytest**
* 🐳 **Docker** containerization
* 🔄 **GitHub Actions CI/CD**
* ☁️ Cloud deployment using **Render**
* ✅ Input validation using **Pydantic**
* 📦 Model persistence and reusable preprocessing pipeline
* 📉 ML model evaluation and performance tracking

---

# 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │       Client        │
                         │  Browser / Postman  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │      REST API       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   JWT Middleware    │
                         │   Authentication    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Request Middleware │
                         │ Logging / Timing    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Redis Cache      │
                         │ Fast Repeated Calls │
                         └──────────┬──────────┘
                                    │
                         Cache Hit ─┤
                                    │ Cache Miss
                                    ▼
                         ┌─────────────────────┐
                         │    ML Pipeline      │
                         │ Preprocessing       │
                         │ + Model Inference   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Price Prediction  │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴────────────────┐
                    ▼                                ▼
          ┌─────────────────┐              ┌─────────────────┐
          │   Prometheus    │              │      Logs       │
          │    Metrics      │              │   Application   │
          └────────┬────────┘              └─────────────────┘
                   │
                   ▼
          ┌─────────────────┐
          │     Grafana     │
          │   Dashboards    │
          └─────────────────┘
```

---

# ✨ Key Features

## 🤖 Machine Learning

The application serves a trained machine learning model through a REST API.

The ML pipeline includes:

* Data preprocessing
* Feature transformation
* Model training
* Model evaluation
* Model persistence
* Prediction inference
* Input validation
* Consistent preprocessing between training and inference

### Model Evaluation

The project evaluates the model using standard regression metrics such as:

* **MAE — Mean Absolute Error**
* **RMSE — Root Mean Squared Error**
* **R² Score**

This makes it possible to evaluate model performance before exposing it through the API.

---

# ⚡ FastAPI Backend

The backend is built using **FastAPI** to provide high-performance asynchronous REST APIs.

Example endpoints:

```text
GET  /health
POST /auth/login
POST /predict
GET  /metrics
```

The API follows a modular structure so authentication, prediction, middleware, and monitoring logic remain separated.

---

# 🔐 JWT Authentication

The API uses **JSON Web Tokens (JWT)** to protect authenticated endpoints.

Authentication flow:

```text
User
 │
 │ Login credentials
 ▼
/auth/login
 │
 ▼
JWT Token
 │
 │ Authorization: Bearer <token>
 ▼
Protected API
 │
 ▼
Prediction
```

This prevents unauthorized users from accessing protected prediction endpoints.

---

# ⚡ Redis Caching

Redis is used as a caching layer to avoid unnecessary repeated model inference.

### Without Cache

```text
Request
   ↓
FastAPI
   ↓
ML Pipeline
   ↓
Model Inference
   ↓
Response
```

### With Redis

```text
Request
   ↓
FastAPI
   ↓
Redis
 ┌─┴───────────────┐
 │                 │
Hit              Miss
 │                 │
 ▼                 ▼
Response       ML Model
                 │
                 ▼
              Redis
                 │
                 ▼
              Response
```

For identical prediction requests, the cached result can be returned directly, reducing computation and improving response latency.

---

# 📊 Monitoring & Observability

The application exposes metrics using **Prometheus** and visualizes them through **Grafana**.

The monitoring stack can be used to observe:

* Request count
* Request latency
* HTTP status codes
* Error rates
* API throughput
* Prediction endpoint performance
* Application health

Example:

```text
FastAPI
   │
   │ /metrics
   ▼
Prometheus
   │
   ▼
Grafana Dashboard
```

This provides visibility into how the ML API behaves in a deployed environment.

---

# 🧩 Middleware

Custom FastAPI middleware is implemented for cross-cutting backend concerns such as:

* Request/response processing
* Request timing
* Logging
* Performance tracking
* Error handling

Example:

```text
Incoming Request
       ↓
Middleware
       ↓
Authentication
       ↓
API Endpoint
       ↓
ML Prediction
       ↓
Middleware
       ↓
Response
```

---

# 🧪 Testing

The project includes automated tests using **Pytest**.

Testing covers areas such as:

* API endpoints
* Authentication
* Prediction responses
* Input validation
* Error handling
* Backend functionality

Run tests using:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

---

# 🐳 Docker

The application is containerized using Docker to provide a consistent runtime environment.

Build the image:

```bash
docker build -t car-price-api .
```

Run the container:

```bash
docker run -p 8000:8000 car-price-api
```

The application can then be accessed at:

```text
http://localhost:8000
```

---

# 🔄 CI/CD

GitHub Actions is used to automate the development workflow.

Typical pipeline:

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Deploy
```

This helps ensure that changes are tested before being deployed.

---

# ☁️ Deployment

The application is deployed using **Render**.

### Production Flow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Docker Build
    │
    ▼
Render
    │
    ▼
Production API
```

🌐 **Live API:** [Add your Render URL here]

📚 **API Documentation:** [Add your `/docs` URL here]

---

# 📁 Project Structure

```text
fastapi_ml-project/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── prediction.py
│   │
│   ├── middleware/
│   │   └── logging_middleware.py
│   │
│   ├── models/
│   │   └── model.pkl
│   │
│   ├── schemas/
│   │   └── prediction.py
│   │
│   └── services/
│       ├── prediction_service.py
│       └── cache_service.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_prediction.py
│   └── test_health.py
│
├── notebooks/
│   └── model_training.ipynb
│
├── data/
│   └── dataset.csv
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── prometheus.yml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
└── README.md
```

> Adjust the structure above to match your actual repository.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Rohit2332000/FastApi-Project.git
```

```bash
cd FastApi-Project
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv myenv
```

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv myenv
```

```bash
source myenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256

REDIS_HOST=localhost
REDIS_PORT=6379

MODEL_PATH=path/to/model.pkl
```

> Never commit real secrets or credentials to GitHub.

---

# ▶️ Run Locally

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 📈 Prometheus

Prometheus scrapes application metrics from:

```text
/metrics
```

Example:

```text
http://localhost:8000/metrics
```

Configure Prometheus to scrape the FastAPI application:

```yaml
scrape_configs:
  - job_name: "fastapi"
    static_configs:
      - targets: ["fastapi-app:8000"]
```

---

# 📊 Grafana

After starting Grafana, open:

```text
http://localhost:3000
```

Add Prometheus as a data source and create dashboards to monitor the application.

Recommended dashboard panels:

* Request Rate
* Average Latency
* P95 Latency
* Error Rate
* HTTP Status Codes
* Endpoint Usage
* Prediction Requests

---

# 🔑 API Usage

## Login

```http
POST /auth/login
```

Example request:

```json
{
  "username": "user",
  "password": "password"
}
```

Response:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

## Predict Car Price

```http
POST /predict
```

Authorization:

```text
Authorization: Bearer <JWT_TOKEN>
```

Example request:

```json
{
  "year": 2022,
  "km_driven": 25000,
  "fuel": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual"
}
```

Example response:

```json
{
  "predicted_price": 850000
}
```

> Update the request fields and response according to your actual model schema.

---

# 🔒 Security Considerations

The project follows several backend security practices:

* JWT-based authentication
* Environment-based secret management
* Input validation using Pydantic
* Protected prediction endpoints
* No hardcoded production credentials
* Controlled API access

---

# ⚙️ Performance Optimization

The backend incorporates several performance-focused techniques:

### Redis Caching

Avoids repeated ML inference for identical requests.

### Middleware Timing

Tracks API execution time.

### Prometheus Metrics

Provides quantitative performance monitoring.

### Efficient ML Inference

The trained model is loaded once rather than retrained for every request.

---

# 📌 Engineering Highlights

This project demonstrates practical experience across multiple layers of modern ML backend engineering:

```text
Machine Learning
      ↓
Model Serving
      ↓
FastAPI
      ↓
Authentication
      ↓
Caching
      ↓
Testing
      ↓
Containerization
      ↓
Monitoring
      ↓
CI/CD
      ↓
Cloud Deployment
```

The goal was to build a system closer to how an ML model would be served in a real production environment.

---

# 🛣️ Future Improvements

Planned improvements include:

* [ ] Model versioning
* [ ] Automated model retraining
* [ ] ML/data drift detection
* [ ] Rate limiting
* [ ] Advanced API load testing
* [ ] Distributed caching
* [ ] Database integration
* [ ] Kubernetes deployment
* [ ] Automated model monitoring
* [ ] Cloud-based ML pipeline
* [ ] Advanced CI/CD deployment strategies

---

# 🎯 What I Learned

Through this project, I gained practical experience in:

* Building production-style APIs with FastAPI
* Serving ML models through REST APIs
* Implementing JWT authentication
* Designing reusable middleware
* Improving API performance using Redis
* Monitoring APIs using Prometheus and Grafana
* Writing automated backend tests
* Containerizing applications with Docker
* Implementing CI/CD pipelines
* Deploying ML applications to the cloud
* Thinking about ML systems beyond model training

---

# 👨‍💻 Author

**Rohit Kumar Yadav**

AI Engineer | GenAI | Agentic AI | ML Backend

🔗 **GitHub:** https://github.com/Rohit2332000

🔗 **Portfolio:** https://rohit2332000.github.io/rohityadav.github.io/

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is available under the MIT License.
