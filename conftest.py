import pytest
from playwright.sync_api import Page # noqa: F401

@pytest.fixture(scope="session")
def base_url():
    """Provides the base URL for the Swag Labs website."""
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def credentials():
    """Provides standard user credentials for Swag Labs."""
    return {"username": "standard_user", "password": "secret_sauce"}

# The 'page' fixture is automatically provided by pytest-playwright plugin.
# It handles browser context and page creation/teardown for each test function.
