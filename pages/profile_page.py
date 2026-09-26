import allure
from locators.profile_locators import ProfileLocators as locator
from pages.base_page import BasePage


class ProfilePage(BasePage):

    def wait_for_authorization_screen(self):
        self.wait_for_element(locator.auth_create_profile_button)

    def wait_for_login_screen(self):
        self.wait_for_element(locator.login_button)

    @allure.step('Клик на кнопку создания профиля в хедере')
    def click_on_create_profile_header(self):
        self.wait_for_element(locator.header_create_profile_button)
        self.click_on_element(locator.header_create_profile_button)

    @allure.step('Клик на кнопку логина в хедере')
    def click_on_login_header(self):
        self.wait_for_element(locator.header_login_button)
        self.click_on_element(locator.header_login_button)

    @allure.step('Заполнение поля email')
    def fill_email_login_screen(self, email):
        self.input_text(locator.login_mail_input, email)

    @allure.step('Заполнение поля Пароль')
    def fill_password_login_screen(self, password):
        self.input_text(locator.login_password_input, password)

    @allure.step('Клик на кнопку входа')
    def click_on_login_button(self):
        self.click_on_element(locator.login_button)

    @allure.step('Заполнение поля Имя')
    def fill_name_auth_screen(self, name):
        self.input_text(locator.auth_name_input, name)

    @allure.step('Заполнение поля Фамилия')
    def fill_secondname_auth_screen(self, secondname):
        self.input_text(locator.auth_secondname_input, secondname)

    @allure.step('Заполнение поля Имя пользователя')
    def fill_username_auth_screen(self, username):
        self.input_text(locator.auth_username_input, username)

    @allure.step('Заполнение поля email')
    def fill_mail_auth_screen(self, mail):
        self.input_text(locator.auth_mail_input, mail)

    @allure.step('Заполнение поля Пароль')
    def fill_password_auth_screen(self, password):
        self.input_text(locator.auth_password_input, password)

    @allure.step('Клик на кнопку создания пользователя')
    def click_on_authorization_button(self):
        self.click_on_element(locator.auth_create_profile_button)

    @allure.step('Полное заполнение формы авторизации')
    def fill_the_entire_authorization_form(self, name, secondname, username, mail, password):
        self.click_on_create_profile_header()
        self.wait_for_authorization_screen()
        self.fill_name_auth_screen(name)
        self.fill_secondname_auth_screen(secondname)
        self.fill_username_auth_screen(username)
        self.fill_mail_auth_screen(mail)
        self.fill_password_auth_screen(password)
        self.click_on_authorization_button()
        self.wait_for_login_screen()

    @allure.step('Полное заполнение формы логина')
    def fill_the_entire_login_form(self, username, password):
        self.wait_for_login_screen()
        self.fill_email_login_screen(username)
        self.fill_password_login_screen(password)
        self.click_on_login_button()
        self.wait_for_element(locator.header_log_out_button)

    def check_authorization_success(self):
        return self.check_visibility(locator.login_button)

    def check_login_success(self):
        return self.check_visibility(locator.header_log_out_button)

    def check_login_success_main_screen(self):
        return self.check_visibility(locator.login_check)

    @allure.step('Создание пользователя и логин')
    def create_profile_and_login(self, name, secondname, username, mail, password):
        self.fill_the_entire_authorization_form(name, secondname, username, mail, password)
        self.fill_the_entire_login_form(username, password)