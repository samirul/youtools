import json
import pytest
from django.db import connection
from django.core.cache import cache
from django.core import mail


@pytest.fixture(autouse=True)
def clean_cache_and_db():
    # clear cache before each test
    cache.clear()

    # make database changes are fully committed
    if connection.in_atomic_block:
        connection.commit()

    # Reset the mail.outbox
    mail.outbox = []

@pytest.mark.django_db(transaction=True)
def test_product_views_if_no_data(client, login):
    cache.delete(f'django_drf_products_cache_{login["user"].get("pk")}')
    headers = {
        "Content-Type": "application/json",
    }
    response = client.get("/api/products/product-items/", headers=headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert len(data.get('data')) == 0
    assert 'id' not in data.get('data')
    assert 'product_image' not in data.get('data')
    assert 'product_name' not in data.get('data')
    assert 'product_description' not in data.get('data')
    assert 'product_url' not in data.get('data')
    assert response.status_code == 200