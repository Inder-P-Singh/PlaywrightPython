# Playwright Python Swag Labs UI Automation Framework

This project provides a UI test automation framework for the Swag Labs website (https://www.saucedemo.com/) using Playwright and Pytest. It demonstrates automating the login and add-to-cart workflows, adhering to the Page Object Model (POM) design pattern for maintainability and scalability.

## Features

*   **Page Object Model (POM):** Clearly separated page interactions and elements for better organization.
*   **Playwright:** Uses Playwright's robust browser automation capabilities for reliable UI testing.
*   **Pytest:** Uses Pytest as the test runner for easy test discovery, execution, and reporting.
*   **Login Workflow:** Tests successful and unsuccessful login scenarios.
*   **Add-to-Cart Workflow:** Tests adding an item to the cart and verifying its presence.
*   **Reporting:** Configured to generate HTML test reports.

## Project Structure

```
.                       (project root)
├── pytest.ini          (Pytest configuration)
├── conftest.py         (Pytest fixtures for browser setup, URLs, credentials)
├── pages/              (Contains Page Object Model classes)
│   ├── __init__.py
│   ├── base_page.py    (Base class for all page objects)
│   ├── login_page.py   (Page object for the login page)
│   ├── products_page.py(Page object for the products inventory page)
│   └── cart_page.py    (Page object for the shopping cart page)
├── tests/              (Contains Pytest test scripts)
│   ├── test_login.py   (Tests for login functionality)
│   └── test_add_to_cart.py (Tests for adding items to cart)
└── test-results/       (Automatically created to store screenshots and reports)
```

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a Python Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows (Command Prompt):
        ```bash
        venv\Scripts\activate.bat
        ```
    *   On Windows (PowerShell):
        ```bash
        venv\Scripts\Activate.ps1
        ```

4.  **Install dependencies:**
    ```bash
    pip install pytest pytest-playwright pytest-html
    ```

5.  **Install Playwright browser binaries:**
    Playwright needs browser binaries to run tests. You can install all common ones:
    ```bash
    playwright install
    ```
    Or install specific browsers, e.g., for Chromium:
    ```bash
    playwright install chromium
    ```

## How to Run Tests

Navigate to the project root directory in your activated virtual environment and run Pytest:

```bash
pytest
```

### Running Tests with Specific Options

*   **Run with a specific browser (e.g., Firefox):**
    ```bash
    pytest --browser=firefox
    ```
*   **Run tests without headless mode (to see the browser UI):**
    ```bash
    pytest --headless=false
    ```
*   **Run only tests related to login:**
    ```bash
    pytest -m login
    ```
*   **Run only tests related to cart:**
    ```bash
    pytest -m cart
    ```

### Viewing Reports

After running tests, an HTML report and XML output will be generated in the `test-results/` directory:

*   **HTML Report:** Open `test-results/report.html` in your web browser.
*   **XML Output:** `test-results/test_results.xml`

Screenshots of key steps are also saved in `test-results/`.

## Page Object Model (POM) Explained

*   **`BasePage`**: Contains methods common to all pages (e.g., `navigate`, `get_current_url`).
*   **`LoginPage`**: Defines locators and methods specific to the Swag Labs login page, suchs as `login()`.
*   **`ProductsPage`**: Defines locators and methods for interacting with the products inventory page, such as `add_item_to_cart()` and `goto_cart()`.
*   **`CartPage`**: Defines locators and methods for interacting with the shopping cart page, such as `get_cart_item_names()`.

Each test in the `tests/` directory imports and utilizes these page objects to perform actions and assertions, making tests readable and maintainable.

## Contact Information
* LinkedIn (11 K Followers, 1.7M Views) https://www.linkedin.com/in/inderpsingh/
* Software and Testing Training channel (355 tutorials, since 2013) https://youtube.com/@QA1/videos
* Software Testing Space blog (1.89 Million Views, 499 Articles and Courses, since 2009) https://inderpsingh.blogspot.com/
