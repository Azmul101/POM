from Config.config import TestData
from Pages.LoginPage import Login
from Test.conftest import BaseTest


class Test_home(BaseTest):

    def test_home_page_tittle(self):
        self.LoginPage = Login(self.driver)
        self.homePage = self.LoginPage.do_login(TestData.User_name, TestData.Password)
        title = self.homePage.get_home_title(TestData.Home_page_title)
        assert title == TestData.Home_page_title

    def test_account_name(self):
        self.LoginPage = Login(self.driver)
        self.homePage = self.LoginPage.do_login(TestData.User_name, TestData.Password)
        header = self.homePage.get_header_value()
        assert header == TestData.Home_page_header

    def test_home_page_header(self):
        self.LoginPage = Login(self.driver)
        self.homePage = self.LoginPage.do_login(TestData.User_name, TestData.Password)
        account = self.homePage.get_account_name_value()
        assert account == TestData.account_name

    def test_setting(self):
        self.LoginPage = Login(self.driver)
        self.homePage = self.LoginPage.do_login(TestData.User_name, TestData.Password)
        assert self.homePage.is_settings_icon_exist()
