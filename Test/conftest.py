import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def driver_init(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.Ch_exe_path)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.Fi_exe_path)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


