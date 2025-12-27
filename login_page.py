from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page object for the Swag Labs login page."""
    URL = "" # Login page is the entry point, so no specific path appended to base_url
    _USERNAME_INPUT = "#user-name"
    _PASSWORD_INPUT = "#password"
    _LOGIN_BUTTON = "#login-button"
    _ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def login(self, username, password):
        """Performs the login action with the given credentials."""
        self.navigate()
        self.page.fill(self._USERNAME_INPUT, username)
        self.page.fill(self._PASSWORD_INPUT, password)
        self.page.click(self._LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Returns the text content of the error message element."""
        return self.page.locator(self._ERROR_MESSAGE).text_content()

    def is_login_successful(self) -> bool:
        """Checks if the user has successfully navigated away from the login page.
        This typically means reaching the products page (inventory.html)."""
        return "inventory.html" in self.get_current_url()
