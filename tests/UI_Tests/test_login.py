import pytest
from playwright.sync_api import sync_playwright
from tests.actions.login_actions import LoginPage
from tests.actions.dashboard_actions import DashboardPage

@pytest.fixture(scope="session")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_login_success(browser_page):
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login("admin", "admin123")  # Replace with valid credentials

    browser_page.wait_for_url("**/dashboard", timeout=5000)

    # Теперь создаём объект DashboardPage
    dashboard_page = DashboardPage(browser_page)
    assert dashboard_page.is_on_dashboard(), "User is not on the dashboard page"
    assert dashboard_page.is_logout_button_visible(), "Logout button is not visible on the dashboard page"

def test_navigate_to_accounts(browser_page):
    dashboard_page = DashboardPage(browser_page)
    dashboard_page.click_to_accounts()
    browser_page.wait_for_url("**/accounts", timeout=5000)
    assert browser_page.url.endswith('/accounts'), "User is not on the accounts page"

def test_navigate_to_transactions(browser_page):
    dashboard_page = DashboardPage(browser_page)
    dashboard_page.click_to_transactions()
    browser_page.wait_for_url("**/transactions", timeout=5000)
    assert browser_page.url.endswith('/transactions'), "User is not on the transactions page"

# def test_logout(browser_page):
#     dashboard_page = DashboardPage(browser_page)
#     dashboard_page.click_logout()
#     login_page = LoginPage(browser_page)
#     assert login_page.is_on_login_page(), "User is not on the login page after logout"

def test_login_failure(browser_page):
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login("wronguser", "wrongpassword")
    assert "Invalid username or password. Please try again." in login_page.get_error_message()