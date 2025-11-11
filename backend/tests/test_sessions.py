from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.exceptions import DoesNotExistError
from app.schemas.auth import TokenData
from unittest.mock import MagicMock, patch

client = TestClient(app)

def test_get_session():
    def override_get_db():
        mock_db = MagicMock()

        mock_session_instance = MagicMock()
        mock_session_instance.id = 1
        mock_session_instance.mentor_id = 1
        mock_session_instance.user_id = 1

        mock_db.query().filter().first.return_value = mock_session_instance
        mock_db.add.return_value = None
        mock_db.commit.return_value = None
        mock_db.refresh.return_value = None
        yield mock_db

    app.dependency_overrides[get_db] = override_get_db

    response = client.get("/sessions/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["mentor_id"] == 1
    assert data["user_id"] == 1

def test_create_session():
    def override_get_db():
        mock_db = MagicMock()

        mock_db.add.return_value = None
        mock_db.commit.return_value = None
        mock_db.refresh.return_value = None
        yield mock_db

    def override_token_decode():
        return TokenData(user_id=2)

    app.dependency_overrides[get_current_user] = override_token_decode
    app.dependency_overrides[get_db] = override_get_db

    with patch("app.crud.session.Session", return_value={}) as mock_session_class:
        mock_session_class.return_value = MagicMock(id=1, mentor_id=1, user_id=1)
        response = client.post("/sessions", json={"mentor_id": 1})
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1

def test_mentor_id_not_found():
    def override_get_db_no_mentor():
        mock_db = MagicMock()
        mock_db.query().filter().first.return_value = None
        yield mock_db

    app.dependency_overrides[get_db] = override_get_db_no_mentor

    with pytest.raises(DoesNotExistError):
        response = client.get("/sessions/999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Session not found"