import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.cart
def test_add_item_to_cart_and_verify(page: Page, base_url: str, credentials):
    """Tests the add-to-cart workflow and verifies the item in the cart."""
    login_page = LoginPage(page, base_url)
    products_page = ProductsPage(page, base_url)
    cart_page = CartPage(page, base_url)

    # 1. Login to the application
    login_page.login(credentials["username"], credentials["password"])
    assert products_page.is_on_page(), "Expected to be on Products page after login."

    # 2. Add an item to the cart
    item_to_add_slug = "backpack" # Corresponds to 'Sauce Labs Backpack'
    item_to_add_full_name = "Sauce Labs Backpack"
    products_page.add_item_to_cart(item_to_add_slug)

    # 3. Verify cart badge count reflects added item
    assert products_page.get_cart_badge_count() == 1, "Cart badge should show 1 item."
    page.screenshot(path="test-results/item_added_to_cart.png")

    # 4. Navigate to the cart page
    products_page.goto_cart()
    assert cart_page.is_on_page(), "Expected to be on Cart page."

    # 5. Verify the item is present in the cart
    cart_items = cart_page.get_cart_item_names()
    assert item_to_add_full_name in cart_items, f"Expected '{item_to_add_full_name}' to be in cart but found {cart_items}."
    page.screenshot(path="test-results/item_in_cart.png")
