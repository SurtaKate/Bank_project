from Bank_project.locators.dashboard_locators import DashboardLocators

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def is_on_dashboard(self):
        # return self.page.url.endswith('https://qatesting.vercel.app/bank/dashboard')
        return self.page.url.endswith('https://qatesting.vercel.app/bank/dashboard')

    def is_logout_button_visible(self):
        return self.page.is_visible(DashboardLocators.LOGOUT_BUTTON)

    def click_to_accounts(self):
        self.page.click(DashboardLocators.ACCOUNTS_NAVIGATE_BUTTON)

    def click_to_transactions(self):
        self.page.click(DashboardLocators.TRANSACTIONS_NAVIGATE_BUTTON)

    def click_logout(self):
        self.page.click(DashboardLocators.LOGOUT_BUTTON)

    def is_logout_successful(self):
        return self.page.url.endswith('https://qatesting.vercel.app/bank')