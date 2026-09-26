import allure
from test_data import Auth


class TestProfile():

    @allure.title('Создание нового профиля')
    def test_create_profile(self, profile):
        auth = Auth()
        auth_data = auth.get_auth_data()
        profile.fill_the_entire_authorization_form(name=auth_data.get('name'),
                                                   secondname=auth_data.get('secondname'),
                                                   username=auth_data.get('username'),
                                                   mail=auth_data.get('mail'),
                                                   password=auth_data.get('password'))
        
        assert profile.check_authorization_success()

    @allure.title('Логин пользователя')
    def test_login_positive(self, profile):
        auth = Auth()
        auth_data = auth.get_auth_data()
        profile.fill_the_entire_authorization_form(name=auth_data.get('name'),
                                                    secondname=auth_data.get('secondname'),
                                                    username=auth_data.get('username'),
                                                    mail=auth_data.get('mail'),
                                                    password=auth_data.get('password'))
        profile.fill_the_entire_login_form(auth_data.get('username'), auth_data.get('password'))

        assert profile.check_login_success()
        assert profile.check_login_success_main_screen()