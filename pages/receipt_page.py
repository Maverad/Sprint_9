import allure
from locators.receipt_locators import ReceiptLocators as locator
from pages.base_page import BasePage
from test_data import receipt_data
from pathlib import Path


class ReceiptPage(BasePage):

    def wait_for_receipt_screen(self):
        self.wait_for_element(locator.receipt_screen)

    def wait_for_created_receipt(self):
        self.wait_for_element(locator.receipt_name_after_creation)

    def wait_for_last_receipt(self):
        self.wait_for_element(locator.last_receipt_on_receipt_screen)

    def wait_for_edit_button(self):
        self.wait_for_element(locator.receipt_edit_button)

    def wait_for_delete_receipt_button(self):
        self.wait_for_element(locator.receipt_delete_button)

    def wait_for_create_receipt_screen(self):
        self.wait_for_element(locator.receipt_create_button)

    @allure.step('Клик на создание рецепта в хедере')
    def click_on_create_receipt_header(self):
        self.wait_for_element(locator.header_create_receipt_button)
        self.click_on_element(locator.header_create_receipt_button)
        self.wait_for_create_receipt_screen()

    @allure.step('Клик на Рецепты в хедере')
    def click_on_receipt_header(self):
        self.wait_for_element(locator.header_receipt_button)
        self.click_on_element(locator.header_receipt_button)
        self.wait_for_receipt_screen()

    @allure.step('Заполнение поля Название рецепта')
    def fill_receipt_name(self):
        self.input_text(locator.receipt_name, receipt_data.get('name'))

    @allure.step('Заполнение поля Ингридиенты')
    def fill_receipt_ingredient(self):
        self.input_text(locator.receipt_ingredients, receipt_data.get('ingredient'))
        self.wait_for_element(locator.receipt_ingredients_list)
        self.click_on_element(locator.receipt_ingredients_list)

    @allure.step('Заполнение поля Количество ингридиента')
    def fill_receipt_ingredient_count(self):
        self.input_text(locator.receipt_ingredients_count, receipt_data.get('count'))

    @allure.step('Заполнение поля Время готовки')
    def fill_receipt_cooking_duration(self):
        self.input_text(locator.receipt_cooking_duration, receipt_data.get('duration'))

    @allure.step('Заполнение поля Описание рецепта')
    def fill_receipt_description(self):
        self.input_text(locator.receipt_desctiption, receipt_data.get('description'))

    @allure.step('Добавление изображения')
    def upload_photo(self):
        project_root = Path(__file__).parent.parent
        image_path = project_root / "assets" / "receipt_img.png"
        self.input_text(locator.receipt_upload_photo_input, str(image_path))

    @allure.step('Клик на Создание рецепта')
    def click_on_create_receipt(self):
        self.click_on_element(locator.receipt_create_button)

    @allure.step('Клик на последний созданный рецепт')
    def click_on_last_receipt(self):
        self.click_on_element(locator.last_receipt_on_receipt_screen)

    @allure.step('Клик на кнопку редактирования рецепта')
    def click_on_edit_receipt_button(self):
        self.click_on_element(locator.receipt_edit_button)

    @allure.step('Клик на кнопку удаления рецепта')
    def click_on_delete_receipt_button(self):
        self.click_on_element(locator.receipt_delete_button)

    @allure.step('Клик на кнопку добавления ингридиента')
    def click_on_add_ingredient_button(self):
        self.click_on_element(locator.receipt_add_ingredient)

    @allure.step('Позитивный флоу создания рецепта')
    def fill_the_entire_receipt_form(self):
        self.fill_receipt_name()
        self.fill_receipt_ingredient()
        self.fill_receipt_ingredient_count()
        self.click_on_add_ingredient_button()
        self.fill_receipt_cooking_duration()
        self.fill_receipt_description()
        self.upload_photo()
        self.click_on_create_receipt()
        self.wait_for_created_receipt()

    @allure.step('Полный флоу удаления последнего рецепта')
    def delete_last_receipt(self):
        self.click_on_receipt_header()
        self.wait_for_last_receipt()
        self.click_on_last_receipt()
        self.wait_for_edit_button()
        self.click_on_edit_receipt_button()
        self.wait_for_delete_receipt_button()
        self.click_on_delete_receipt_button()

    def check_create_receipt_name_success(self):
        return self.check_visibility(locator.receipt_name_after_creation)

    def check_create_receipt_card_success(self):
        return self.check_visibility(locator.receipt_card_after_creation)
    