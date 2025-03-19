import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_bottom_banner_cache')

@pytest.mark.django_db()
def test_bottomBanner_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/bottom-banner/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'banner_image' not in data
    assert 'banner_text' not in data
    assert response.status_code == 200

@pytest.mark.django_db()
def test_bottomBanner(client, create_bottom_banner):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/bottom-banner/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'banner_image' in data[0]
    assert 'banner_text' in data[0]

    assert data[0]['banner_image'] == '/media/test_image2.png'
    assert data[0]['banner_text'] == 'this is test bottom banner'
    assert response.status_code == 200