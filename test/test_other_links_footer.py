import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_link_footer_cache')

@pytest.mark.django_db()
def test_links_footer_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/links/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'category_name' not in data
    assert 'name' not in data
    assert response.status_code == 200

@pytest.mark.django_db()
def test_links_footer(client, create_link_footer):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/links/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'category_name' in data[0]
    assert 'name' in data[0]
    assert 'id' in data[0].get('name')[0]
    assert 'links_title' in data[0].get('name')[0]
    assert 'links_url' in data[0].get('name')[0]

    assert data[0]['category_name'] == 'test_link_footer_category'
    assert data[0].get('name')[0]['links_title'] == 'test_link_title'
    assert data[0].get('name')[0]['links_url'] == 'test_link_url'
    assert response.status_code == 200

