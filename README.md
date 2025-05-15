# 🚀 GitHub Actions CI/CD for Python Web App with Docker & Azure Deployment

This repository sets up a complete CI/CD pipeline using **GitHub Actions** to lint, test, scan, containerize, and deploy a Python web application to **Azure Web App**. The app is containerized using a custom `Dockerfile`, and key endpoints are verified with unit tests using `pytest`.

---

## 📦 What's Included?

- ✅ Code linting with `flake8`
- 🧪 Unit testing with `pytest`
- 🛡️ Security scanning using [Trivy](https://github.com/aquasecurity/trivy)
- 🐳 Docker image building & publishing to GitHub Container Registry (GHCR)
- ☁️ Deployment to Azure Web App via GitHub Actions

---

## ⚙️ CI/CD Workflow Overview

### 🔍 `build_test_code`

Triggered on push or PR to the `main` branch:
- Sets up Python 3.10
- Installs dependencies from `requirements.txt`
- Lints code using `flake8`
- Runs `pytest` tests
- Scans the source code with Trivy for critical vulnerabilities
- Uploads SARIF report to GitHub Security tab

### 🛠️ `build_docker_image`

Triggered after successful code tests:
- Builds and pushes Docker image using [Docker Buildx](https://github.com/docker/build-push-action)
- Pushes image to **GitHub Container Registry**

### 🚀 `deploy_image`

Triggered after Docker image is built:
- Deploys the containerized app to **Azure Web App** using your publish profile

---

## 🧪 Pytest Tests

The repository includes basic unit tests to verify endpoint functionality. These are located in your test suite and executed during the `build_test_code` job.

### ✅ `test_healthz`

```python
import pytest
from app.app import app  # Update as needed if your Flask file name differs

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.data.decode() == "OK"
```

### 🚫 `test_404_route`

```python
import pytest
from app.app import app  

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_404_route(client):
    response = client.get("/non-existent-endpoint")
    assert response.status_code == 404
    assert b"Not Found" in response.data  # Optional content check
```

These tests verify the availability of a health check endpoint and the app's behavior on invalid routes.

---

## 🐳 Dockerfile Overview

Your application is containerized using the following `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy all source code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Expose the port Flask runs on
EXPOSE 5000

# Run the app using Flask CLI
CMD ["flask", "run"]
```

📌 Ensure your Flask entry point is located at `app/app.py`.

---

## 🔐 Required GitHub Secrets

| Secret Name                   | Description                                           |
|------------------------------|-------------------------------------------------------|
| `AZURE_WEBAPP_PUBLISH_PROFILE` | Azure publish profile (download from Azure portal) |

---

## 🌍 Environment Variables in Workflow

| Variable                     | Description                                                   |
|-----------------------------|---------------------------------------------------------------|
| `REGISTRY`                  | Docker registry (default: `ghcr.io`)                          |
| `IMAGE_NAME`                | Docker image name derived from the repository                 |
| `AZURE_WEBAPP_NAME`         | Azure Web App name (e.g., `ProaTest`)                         |
| `AZURE_WEBAPP_PACKAGE_PATH` | Path to the app code inside the repo (default: root directory)|

---

## 🚀 Getting Started

1. Set up your Azure Web App.
2. Download its publish profile and add it to GitHub secrets as `AZURE_WEBAPP_PUBLISH_PROFILE`.
3. Adjust `AZURE_WEBAPP_NAME` in the workflow YAML file.
4. Push code to `main` — GitHub Actions takes care of testing, scanning, building, and deploying.

---

## 📂 Key Files

| File/Directory                     | Purpose                                          |
|-----------------------------------|--------------------------------------------------|
| `.github/workflows/python-app.yml`| CI/CD workflow definition                        |
| `Dockerfile`                      | Container definition for the Flask app           |
| `tests/` (recommended)            | Directory for pytest-based unit tests            |
| `app/app.py`                      | Flask application entry point                    |

---

## 📄 License

This project is open-source. You can use it freely under the terms of your chosen license (e.g., MIT, Apache-2.0).
