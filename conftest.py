import pytest
from selenium import webdriver
from pages.profile_page import ProfilePage
from pages.receipt_page import ReceiptPage
from test_data import Auth
from test_data import Urls

@pytest.fixture
def driver():
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=webdriver.ChromeOptions()
    )
    driver.get(Urls.base_url)
    yield driver
    driver.quit()

@pytest.fixture
def profile_auth(driver):
    profile = ProfilePage(driver)
    auth = Auth()
    auth_data = auth.get_auth_data()
    profile.create_profile_and_login(name=auth_data.get('name'),
                                    secondname=auth_data.get('secondname'),
                                    username=auth_data.get('username'),
                                    mail=auth_data.get('mail'),
                                    password=auth_data.get('password'))
    return profile

@pytest.fixture
def profile(driver) -> ProfilePage:
    profile = ProfilePage(driver)
    return profile

@pytest.fixture
def receipt(driver):
    receipt = ReceiptPage(driver)
    yield receipt
    # Удаление рецепта
