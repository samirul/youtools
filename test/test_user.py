import json
import pytest
import redis
from django.core import mail

red = redis.Redis(decode_responses=True)

@pytest.mark.django_db()
def test_register(client):
    response = client.post("/api/registration/", {
        "email": "cat@cat.com",
        "password1": "cat&koop123",
        "password2": "cat&koop123"
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert "detail" in data
    assert "Verification e-mail sent." in data['detail']
    assert response.status_code == 201
    assert len(mail.outbox) == 1  # Check if email was sent
    email = mail.outbox[0]

    verification_link = next(
        line for line in email.body.splitlines() if "http" in line
    )

    data = verification_link.split()
    path_components = data[4].split('/')
    path_components = [component for component in path_components if component]
    verify_response = client.post(f"http://0.0.0.0:8000/accounts/accounts/confirm-email/{path_components[5]}/")
    assert verify_response.status_code == 302
    assert verify_response.url == "/accounts/profile/"


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "register", 
    [{"email": "cat1@cat.com", "password": "cat2&koop123", "confirm_password": "cat2&koop123"}], 
    indirect=True
)
def test_login(client, register):
    response = client.post("/api/auth/login/",{
        "email": "cat1@cat.com",
        "password": "cat2&koop123",
    })

    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'access' in data
    assert 'refresh' in data
    assert 'user' in data
    assert 'pk' in data['user']
    assert 'email' in data['user']
    assert response.status_code == 200
    red.set("flask_cache_test_user_key", data['access'])
    red.set("flask_cache_test_user_info", str(data['user']))





@pytest.mark.django_db()
@pytest.mark.parametrize(
    "register", 
    [{"email": "cat2@cat.com", "password": "cat4&koop123", "confirm_password": "cat4&koop123"}], 
    indirect=True
)
def test_login_failed_wrong_password(client, register):
    response = client.post("/api/auth/login/",{
        "email": "cat2@cat.com",
        "password": "cat3&koop123",
    })

    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert not 'access' in data
    assert not 'refresh' in data
    assert not 'user' in data
    assert 'non_field_errors' in data
    assert ['Unable to log in with provided credentials.'] == data['non_field_errors']
    assert response.status_code == 400
