from helpers import GenerateTestData as GD

class Urls:
    base_url = "https://foodgram-frontend-1.foodgram.education-services.ru/signin"

class Auth:

    def get_auth_data(self):
        generate = GD()
        authorization = {
                "name": generate.generate_random_name(),
                "secondname": generate.generate_random_name(),
                "username": generate.generate_random_name(),
                "mail": generate.generate_random_email(),
                "password": generate.generate_random_password()
            }
        return authorization

receipt_data = {
    "name": "Тестовый рецепт",
    "ingredient": "горчица",
    "duration": "30",
    "count": "5",
    "description": "Тестовое описание рецепта"
}