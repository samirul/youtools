import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_top_banner_cache')

@pytest.mark.django_db()
def test_topBanner_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/top-banner/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'banner_image' not in data
    assert 'banner_text' not in data
    assert response.status_code == 200

@pytest.mark.django_db()
def test_topBanner(client, create_top_banner):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/top-banner/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'banner_image' in data[0]
    assert 'banner_text' in data[0]

    assert data[0]['banner_image'] == '/media/test_image.png'
    assert data[0]['banner_text'] == 'this is test top banner'
    assert response.status_code == 200