from playwright.sync_api import Page
from Bank_project.locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://qatesting.vercel.app/bank")

    def login(self, username: str, password: str):
        self.page.fill(LoginLocators.USERNAME_INPUT, username)
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.text_content(LoginLocators.ERROR_MESSAGE)

    def is_on_login_page(self):
        return self.page.url.endswith('https://qatesting.vercel.app/bank')