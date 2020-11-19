from selenium.webdriver.common.by import By

from Pages.BasePage import Base


class HomePage(Base):
    Header = (By.CSS_SELECTOR, "h1.dashboard-selector_titile")
    Account_Name = (By.CSS_SELECTOR, "account-name")
    Setting_icon = (By.ID, "navSetting")

    def __init__(self, driver):
        self.driver = driver

    def get_home_title(self, title):
        return self.get_title(title)

    def is_settings_icon_exist(self):
        return self.is_visible(self.Setting_icon)

    def get_header_value(self):
        if self.is_visible(self.Header):
            return self.get_element_text(self.Header)

    def get_account_name_value(self):
        if self.is_visible(self.Account_Name):
            return self.get_element_text(self.Account_Name)
