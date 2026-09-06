from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_timeout = 20

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, self.base_timeout).until(EC.visibility_of_element_located((locator)))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def check_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()