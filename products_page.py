from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Page object for the Swag Labs products inventory page."""
    URL = "inventory.html"
    _TITLE_SELECTOR = ".title"
    _ADD_TO_CART_BUTTON_PREFIX = "#add-to-cart-sauce-labs-" # Dynamic part for product name
    _CART_BADGE = ".shopping_cart_badge"
    _CART_LINK = ".shopping_cart_link"
    _PRODUCT_NAMES = ".inventory_item_name"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def is_on_page(self) -> bool:
        """Verifies if the current page is the products page."""
        self.page.wait_for_selector(self._TITLE_SELECTOR)
        return self.page.locator(self._TITLE_SELECTOR).text_content() == "Products"

    def add_item_to_cart(self, item_name_slug: str):
        """Adds a specified item to the cart.
        item_name_slug should be the slugified part of the product name (e.g., 'backpack', 'bike-light')."""
        add_button_locator = f"{self._ADD_TO_CART_BUTTON_PREFIX}{item_name_slug}"
        self.page.click(add_button_locator)

    def get_cart_badge_count(self) -> int:
        """Returns the number of items displayed in the shopping cart badge."""
        badge = self.page.locator(self._CART_BADGE)
        if badge.is_visible():
            return int(badge.text_content())
        return 0

    def goto_cart(self):
        """Navigates to the shopping cart page."""
        self.page.click(self._CART_LINK)
