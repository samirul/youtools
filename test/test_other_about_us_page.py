import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_about-us_page_cache')

@pytest.mark.django_db()
def test_about_us_page_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/about-us/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'title' not in data
    assert 'description' not in data
    assert response.status_code == 200


@pytest.mark.django_db()
def test_about_us_page(client, create_about_us_page):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/about-us/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'title' in data[0]
    assert 'description' in data[0]
    
    assert data[0]['title'] == 'test_about_us_title'
    assert data[0]['description'] == 'test_about_us_description'
    assert response.status_code == 200