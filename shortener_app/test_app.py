import pytest
from fastapi.testclient import TestClient
from .main import app
import requests

client = TestClient(app)

# Test for the root endpoint (GET /)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the URL Shortener!"

# Test creating a shortened URL with a valid target URL
def test_create_url_valid():
    url_data = {"target_url": "https://www.apple.com"}
    response = client.post("/url", json=url_data)
    assert response.status_code == 200
    
    # Extract response data
    response_data = response.json()
    
    # Check that the generated URL starts with the base URL of the API
    assert response_data["url"].startswith("http://127.0.0.1:8000/")
    
    # Ensure that the generated key has the expected length
    assert len(response_data["url"].split("/")[-1]) == 5

# Test creating a shortened URL with a missing 'target_url' field
def test_create_url_missing_target_url():
    url_data = {}
    response = client.post("/url", json=url_data)
    
    # Expect a 422 Unprocessable Entity response since 'target_url' is required
    assert response.status_code == 422
    
    # Extract response data and verify error details
    response_data = response.json()
    assert response_data["detail"][0]["msg"] == "field required"  # Expected FastAPI error message
    assert response_data["detail"][0]["loc"] == ["body", "target_url"]  # Ensure the error is related to the 'target_url' field
