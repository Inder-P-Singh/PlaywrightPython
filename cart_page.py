from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page object for the Swag Labs shopping cart page."""
    URL = "cart.html"
    _TITLE_SELECTOR = ".title"
    _CART_ITEM_NAME_SELECTOR = ".inventory_item_name"
    _CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def is_on_page(self) -> bool:
        """Verifies if the current page is the cart page."""
        self.page.wait_for_selector(self._TITLE_SELECTOR)
        return self.page.locator(self._TITLE_SELECTOR).text_content() == "Your Cart"

    def get_cart_item_names(self) -> list[str]:
        """Returns a list of names of items currently in the cart."""
        return [name.text_content() for name in self.page.locator(self._CART_ITEM_NAME_SELECTOR).all()]

    def checkout(self):
        """Clicks the checkout button."""
        self.page.click(self._CHECKOUT_BUTTON)
