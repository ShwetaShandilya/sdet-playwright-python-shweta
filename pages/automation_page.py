from pages.base_page import BasePage


class AutomationPage(BasePage):

    def navigate_to_homepage(self, base_url):
        self.navigate(base_url)

    def get_homepage_title(self):
        return self.get_title()