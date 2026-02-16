class accounts_page:
    def __init__(self, page):
        self.page = page

    def is_on_accounts_page(self):
        return self.page.url.endswith('https://qatesting.vercel.app/bank/accounts')
