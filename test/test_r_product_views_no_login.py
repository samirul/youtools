import json
import pytest

@pytest.mark.django_db(transaction=True)
def test_product_views_if_no_login(client):
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/products/product-items/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert data.get('detail') == 'Authentication credentials were not provided.'
    assert response.status_code == 401