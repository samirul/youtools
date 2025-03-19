import json
import pytest
from django.core import mail
from django.test import Client
from others.models import *
from products.models import *

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def register(client, request):
    response = client.post("/api/registration/", {
        "email": request.param.get("email"),
        "password1": request.param.get("password"),
        "password2": request.param.get("confirm_password")
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    email = mail.outbox[0]

    verification_link = next(
        line for line in email.body.splitlines() if "http" in line
    )

    data = verification_link.split()
    path_components = data[4].split('/')
    path_components = [component for component in path_components if component]
    verify_response = client.post(f"http://0.0.0.0:8000/accounts/accounts/confirm-email/{path_components[5]}/")
    return verify_response

@pytest.fixture
def user_register(client, settings):
    response = client.post("/api/registration/", {
        "email": "cat@cat.com",
        "password1": "cat&koop123",
        "password2": "cat&koop123"
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    email = mail.outbox[0]
    verification_link = next(
        line for line in email.body.splitlines() if "http" in line
    )
    data = verification_link.split()
    path_components = data[4].split('/')
    path_components = [component for component in path_components if component]
    verify_response = client.post(f"http://0.0.0.0:8000/accounts/accounts/confirm-email/{path_components[5]}/")

@pytest.fixture
def login(client, user_register):
    response = client.post("/api/auth/login/",{
        "email": "cat@cat.com",
        "password": "cat&koop123",
    })

    content = response.content.decode('utf-8')
    data = json.loads(content)
    return data

@pytest.fixture
def create_top_banner():
    top_banner = TopBanner.objects.create(banner_image="test_image.png",
                           banner_text="this is test top banner")
    return top_banner


@pytest.fixture
def create_bottom_banner():
    bottom_banner = BottomBanner.objects.create(banner_image="test_image2.png",
                           banner_text="this is test bottom banner")
    return bottom_banner

@pytest.fixture
def create_link_footer_category():
    links_footer_category = LinksFooterCategory.objects.create(category_name="test_link_footer_category")
    return links_footer_category

@pytest.fixture
def create_link_footer(create_link_footer_category):
    links_footer = LinksFooter.objects.create(links_title="test_link_title",
                             links_url="test_link_url",
                             category=create_link_footer_category)
    return links_footer

@pytest.fixture
def create_social_link_footer_category():
    links_social_footer_category = SocialLinksFooterCategory.objects.create(
        social_category_name="test_social_category"
    )
    return links_social_footer_category

@pytest.fixture
def create_social_link_footer(create_social_link_footer_category):
    social_links_footer = SocialLinksFooter.objects.create(
        social_icon="test_Social_icon.png",
        social_url="test_social_url",
        social_label="test_social_label",
        category=create_social_link_footer_category
    )
    return social_links_footer

@pytest.fixture
def create_title_footer():
    title_footer = TitleFooter.objects.create(
        footer_title="test_footer_title",
        footer_description="test_footer_description"
    )
    return title_footer

@pytest.fixture
def create_copyright_footer():
    copyright_title_footer = CopyRightFooter.objects.create(
        copyright_footer="test_copyright_footer_title"
    )
    return copyright_title_footer

@pytest.fixture
def create_about_us_page():
    about_us = AboutUs.objects.create(
        title="test_about_us_title",
        description="test_about_us_description"
    )
    return about_us

@pytest.fixture
def create_privacy_policy_page():
    privacy_policy = PrivacyPolicy.objects.create(
        title="test_privacy_policy_title",
        description="test_privacy_policy_description"
    )
    return privacy_policy

@pytest.fixture
def create_product_banner():
    products = ProductList.objects.create(
        product_image = "products/images/test_cat_image.png",
        product_name = "test_cat_product_name",
        product_description = "test_cat_product_description",
        product_url = "test_cat_url"
    )
    return products
