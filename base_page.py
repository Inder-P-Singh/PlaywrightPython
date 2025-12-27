from playwright.sync_api import Page

class BasePage:
    """Base class for all Page Objects, providing common functionalities."""
    URL = None # To be overridden by subclasses with their specific path

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        """Navigates to the page's specific URL or the base URL if none specified."""
        if self.URL is not None:
            self.page.goto(f"{self.base_url}{self.URL}")
        else:
            self.page.goto(self.base_url)

    def get_current_url(self) -> str:
        """Returns the current URL of the page."""
        return self.page.url
