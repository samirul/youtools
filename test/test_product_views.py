import json
import pytest

@pytest.mark.django_db()
def test_product_views(client, login, create_product_banner):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/products/product-items/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data.get('data')[0]
    assert 'product_image' in data.get('data')[0]
    assert 'product_name' in data.get('data')[0]
    assert 'product_description' in data.get('data')[0]
    assert 'product_url' in data.get('data')[0]

    assert data.get('data')[0]['product_image'] == '/media/products/images/test_cat_image.png'
    assert data.get('data')[0]['product_name'] == 'test_cat_product_name'
    assert data.get('data')[0]['product_description'] == 'test_cat_product_description'
    assert data.get('data')[0]['product_url'] == 'test_cat_url'
    assert response.status_code == 200