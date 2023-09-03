# tests/test_middleware.py
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_response_time import ResponseTimeMiddleware

app = FastAPI()
app.add_middleware(ResponseTimeMiddleware)
client = TestClient(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def test_response_time_header():
    response = client.get("/")
    assert response.status_code == 200
    assert "x-response-time" in response.headers
    # ... further tests related to the value, format, etc. of the header.
