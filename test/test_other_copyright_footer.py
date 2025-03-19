import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_copyright_footer_cache')

@pytest.mark.django_db()
def test_copyright_footer_if_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/copyright-text/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'copyright_footer' not in data
    assert response.status_code == 200


@pytest.mark.django_db()
def test_copyright_footer(client, create_copyright_footer):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/copyright-text/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'copyright_footer' in data[0]
    
    assert data[0]['copyright_footer'] == 'test_copyright_footer_title'
    assert response.status_code == 200