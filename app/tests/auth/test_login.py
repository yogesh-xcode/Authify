from starlette.testclient import TestClient
from pydantic import ValidationError
import pytest

from app.main import app
from app.models.response_model import SuccessResponse
from app.tests.models.validate_error_model import ErrorResponse


def test_login_success():
    with TestClient(app) as client:  # this triggers lifespan
        response = client.post(
            "/auth/login",
            json={"email": "admin0909@gmail.com", "password": "admin0909"},
        )

        assert (
            response.status_code == 202
        ), f"expected 202 but got {response.status_code}"
        try:
            response_data = response.json()
            SuccessResponse(**response_data)
        except ValidationError:
            pytest.fail("response body is not as the format intended.")
        except Exception as e:
            pytest.fail(f"failed due to unknown reason: {e}")


def test_login_fail():
    with TestClient(app) as client:  # this triggers lifespan
        response = client.post(
            "/auth/login",
            json={"email": "imposter0909@gmail.com", "password": "imposter0909"},
        )

        assert (
            response.status_code == 401
        ), f"expected 401 but got {response.status_code}"
        try:
            response_data = response.json()
            ErrorResponse(**response_data)
        except ValidationError:
            pytest.fail("response body is not as the format intended.")
        except Exception as e:
            pytest.fail(f"failed due to unknown reason")


def test_login_missing_fields():
    with TestClient(app) as client:
        response = client.post(
            "/auth/login",
            json={"email": "admin0909@gmail.com"},
        )

        assert (
            response.status_code == 422
        ), f"expected 422 but got {response.status_code}"
