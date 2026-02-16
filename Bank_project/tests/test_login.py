import pytest
from playwright.sync_api import sync_playwright
from Bank_project.actions.login_actions import LoginPage
from Bank_project.actions.dashboard_actions import DashboardPage
from Bank_project.utils.credentials import Credentials

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_e2e_valid_login_and_navigation(browser_page):
    # 1. Логин
    login_page = LoginPage(browser_page)
    login_page.navigate()
    username = Credentials.get_username()
    password = Credentials.get_password()
    login_page.login(username, password)

    browser_page.wait_for_url("**/dashboard", timeout=5000)
    dashboard_page = DashboardPage(browser_page)
    assert dashboard_page.is_on_dashboard(), "User is not on the dashboard page"
    assert dashboard_page.is_logout_button_visible(), "Logout button is not visible on the dashboard page"

    # 2. Навигация на страницу транзакций
    dashboard_page.click_to_transactions()
    browser_page.wait_for_url("**/transactions", timeout=5000)
    assert browser_page.url.endswith('/transactions'), "User is not on the transactions page"

    # 3. Навигация на страницу аккаунтов
    dashboard_page.click_to_accounts()
    browser_page.wait_for_url("**/accounts", timeout=5000)
    assert browser_page.url.endswith('/accounts'), "User is not on the accounts page"

def test_e2e_invalid_login(browser_page):
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login("wronguser", "wrongpassword")
    assert "Invalid username or password. Please try again." in login_page.get_error_message()