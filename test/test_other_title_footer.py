import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_title_footer_cache')

@pytest.mark.django_db()
def test_title_footer_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/footer-title/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'footer_title' not in data
    assert 'footer_description' not in data
    assert response.status_code == 200


@pytest.mark.django_db()
def test_title_footer(client, create_title_footer):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/footer-title/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'footer_title' in data[0]
    assert 'footer_description' in data[0]
    
    assert data[0]['footer_title'] == 'test_footer_title'
    assert data[0]['footer_description'] == 'test_footer_description'
    assert response.status_code == 200