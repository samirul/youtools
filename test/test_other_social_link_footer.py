import json
import pytest
from django.core.cache import cache

cache.delete('django_drf_social_link_footer_cache')

@pytest.mark.django_db()
def test_social_links_footer_no_data(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/social-links/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data) == 0
    assert 'id' not in data
    assert 'social_category_name' not in data
    assert 'social_data' not in data
    assert response.status_code == 200

@pytest.mark.django_db()
def test_social_links_footer(client, create_social_link_footer):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/others/social-links/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'social_category_name' in data[0]
    assert 'social_data' in data[0]
    assert 'id' in data[0].get('social_data')[0]
    assert 'social_icon' in data[0].get('social_data')[0]
    assert 'social_url' in data[0].get('social_data')[0]
    assert 'social_label' in data[0].get('social_data')[0]

    assert data[0]['social_category_name'] == 'test_social_category'
    assert data[0].get('social_data')[0]['social_icon'] == 'test_Social_icon.png'
    assert data[0].get('social_data')[0]['social_url'] == 'test_social_url'
    assert data[0].get('social_data')[0]['social_label'] == 'test_social_label'
    assert response.status_code == 200