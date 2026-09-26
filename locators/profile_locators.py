from selenium.webdriver.common.by import By


class ProfileLocators:
    # General
    header_login_button = (By.XPATH, ".//a[text()='Войти']")
    header_create_profile_button = (By.XPATH, ".//a[text()='Создать аккаунт']")
    header_log_out_button = (By.XPATH, ".//a[text()='Выход']")

    # Login locators
    login_mail_input = (By.XPATH, ".//input[@name='email']")
    login_password_input = (By.XPATH, ".//input[@name='password']")
    login_button = (By.XPATH, ".//button[text()='Войти']")
    login_check = (By.XPATH, ".//h1[text()='Рецепты']")

    # Authorization locators
    auth_name_input = (By.XPATH, ".//input[@name='first_name']")
    auth_secondname_input = (By.XPATH, ".//input[@name='last_name']")
    auth_username_input = (By.XPATH, ".//input[@name='username']")
    auth_mail_input = (By.XPATH, ".//input[@name='email']")
    auth_password_input = (By.XPATH, ".//input[@name='password']")
    auth_create_profile_button = (By.XPATH, ".//button[text()='Создать аккаунт']")