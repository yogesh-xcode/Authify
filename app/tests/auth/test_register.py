from starlette.testclient import TestClient
from pydantic import ValidationError
import pytest
import random, string
from app.main import app
from app.schemas.response_schema import SuccessResponse
from app.tests.models.validate_error_model import ErrorResponse


def test_register_success():
    with TestClient(app) as client:  # this triggers lifespan
        random_user = "".join(
            random.choices(string.ascii_letters + string.digits, k=14)
        )
        print(random_user)
        response = client.post(
            "/auth/register",
            json={
                "username": random_user,
                "email": f"{random_user}@gmail.com",
                "password": random_user,
            },
        )

        assert (
            response.status_code == 201
        ), f"expected 201 but got {response.status_code}"
        try:
            response_data = response.json()
            SuccessResponse(**response_data)
        except ValidationError:
            pytest.fail("response body is not as the format intended.")
        except Exception as e:
            pytest.fail(f"failed due to unknown reason: {e}")


def test_register_fail():
    with TestClient(app) as client:  # this triggers lifespan
        response = client.post(
            "/auth/register",
            json={
                "username": "admin0909",
                "email": "admin0909@gmail.com",
                "password": "admin0909",
            },
        )

        assert (
            response.status_code == 409
        ), f"expected 409 but got {response.status_code}"
        try:
            response_data = response.json()
            ErrorResponse(**response_data)
        except ValidationError:
            pytest.fail("response body is not as the format intended.")
        except Exception as e:
            pytest.fail(f"failed due to unknown reason")


def test_register_missing_fields():
    with TestClient(app) as client:
        response = client.post(
            "/auth/register",
            json={"email": "admin0707@gmail.com", "password": "admin0707"},
        )

        assert (
            response.status_code == 422
        ), f"expected 422 but got {response.status_code}"
