import pytest

from app import app as flask_app
from app import db
from models import User
from services import UserService


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    flask_app.config["WTF_CSRF_ENABLED"] = False

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    with app.app_context():
        test_users = [
            {
                "gender": "male",
                "name": {"first": "John", "last": "Doe"},
                "phone": "123-456-7890",
                "email": "john@example.com",
                "location": {
                    "street": {"number": 123, "name": "Main St"},
                    "city": "Anytown",
                    "state": "CA",
                    "postcode": "12345",
                },
                "picture": {
                    "thumbnail": "http://example.com/thumb.jpg",
                    "large": "http://example.com/large.jpg",
                },
            }
        ]
        UserService.save_users(test_users)
        yield


def test_index_page(client, init_database):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Random Users" in response.data


def test_user_detail_page(client, init_database):
    with flask_app.app_context():
        user = User.query.first()
        response = client.get(f"/user/{user.id}")
        assert response.status_code == 200
        assert user.first_name.encode() in response.data
        assert user.last_name.encode() in response.data


def test_pagination(client, init_database):
    test_users = [
        {
            "gender": "female",
            "name": {"first": f"Jane{i}", "last": "Smith"},
            "phone": f"555-555-{i:04d}",
            "email": f"jane{i}@example.com",
            "location": {
                "street": {"number": i, "name": "Oak St"},
                "city": "Othertown",
                "state": "NY",
                "postcode": f"5432{i}",
            },
            "picture": {
                "thumbnail": f"http://example.com/thumb{i}.jpg",
                "large": f"http://example.com/large{i}.jpg",
            },
        }
        for i in range(1, 25)
    ]

    with flask_app.app_context():
        UserService.save_users(test_users)

    response = client.get("/")
    assert response.status_code == 200
    assert b"Jane1" in response.data

    response = client.get("/?page=2")
    assert response.status_code == 200
    assert b"Jane20" in response.data


def test_user_service_save_users(app):
    test_user = {
        "gender": "female",
        "name": {"first": "Alice", "last": "Wonderland"},
        "phone": "987-654-3210",
        "email": "alice@example.com",
        "location": {
            "street": {"number": 456, "name": "Elm St"},
            "city": "Wonderland",
            "state": "WL",
            "postcode": "98765",
        },
        "picture": {
            "thumbnail": "http://example.com/alice_thumb.jpg",
            "large": "http://example.com/alice_large.jpg",
        },
    }

    with app.app_context():
        count_before = UserService.get_user_count()
        UserService.save_users([test_user])
        count_after = UserService.get_user_count()
        assert count_after == count_before + 1

        user = User.query.filter_by(first_name="Alice").first()
        assert user is not None
        assert user.last_name == "Wonderland"


def test_user_model_to_dict(app, init_database):
    with app.app_context():
        user = User.query.first()
        user_dict = user.to_dict()
        assert isinstance(user_dict, dict)
        assert "first_name" in user_dict
        assert "last_name" in user_dict
        assert "email" in user_dict
        assert "location" in user_dict
