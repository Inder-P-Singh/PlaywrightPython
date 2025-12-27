import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.login
def test_successful_login(page: Page, base_url: str, credentials):
    """Tests the successful login workflow using valid credentials."""
    login_page = LoginPage(page, base_url)
    products_page = ProductsPage(page, base_url)

    login_page.login(credentials["username"], credentials["password"])

    # Assertions
    assert products_page.is_on_page(), "Expected to be on the Products page after successful login."
    assert login_page.is_login_successful(), "URL should reflect successful login to inventory.html."
    page.screenshot(path="test-results/successful_login.png")

@pytest.mark.login
def test_unsuccessful_login(page: Page, base_url: str):
    """Tests the unsuccessful login workflow using invalid credentials."""
    login_page = LoginPage(page, base_url)

    login_page.login("wrong_user", "wrong_password")

    # Assertions
    assert not login_page.is_login_successful(), "Expected not to be logged in after unsuccessful attempt."
    assert "inventory.html" not in login_page.get_current_url(), "URL should not be inventory.html."
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service",\
        "Expected specific error message for invalid credentials."
    page.screenshot(path="test-results/unsuccessful_login.png")
