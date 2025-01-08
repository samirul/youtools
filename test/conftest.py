import json
import pytest
from django.core import mail
from django.test import Client

@pytest.fixture
def client():
    return Client()


@pytest.fixture
def register(client, request):
    response = client.post("/api/registration/", {
        "email": request.param.get("email"),
        "password1": request.param.get("password"),
        "password2": request.param.get("confirm_password")
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    email = mail.outbox[0]

    verification_link = next(
        line for line in email.body.splitlines() if "http" in line
    )

    data = verification_link.split()
    path_components = data[4].split('/')
    path_components = [component for component in path_components if component]
    verify_response = client.post(f"http://0.0.0.0:8000/accounts/accounts/confirm-email/{path_components[5]}/")
    return verify_response