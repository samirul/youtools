import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_privacy-policy_page_cache')

@pytest.mark.django_db()
def test_privacy_policy_page_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/privacy-policy/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'title' not in data
    assert 'description' not in data
    assert response.status_code == 200


@pytest.mark.django_db()
def test_privacy_policy_page(client, create_privacy_policy_page):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/privacy-policy/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'title' in data[0]
    assert 'description' in data[0]
    
    assert data[0]['title'] == 'test_privacy_policy_title'
    assert data[0]['description'] == 'test_privacy_policy_description'
    assert response.status_code == 200