from selenium.webdriver.common.by import By


class ReceiptLocators:
    # General
    header_receipt_button = (By.XPATH, ".//a[text()='Рецепты']")
    header_create_receipt_button = (By.XPATH, ".//a[text()='Создать рецепт']")

    # Extra
    receipt_screen = (By.XPATH, ".//h1[text()='Рецепты']")
    last_receipt_on_receipt_screen = (By.XPATH, "(.//div[@class='style_card__image__3xIhV'])[1]")

    # Create receipt form 
    receipt_name = (By.XPATH, ".//input[@class='styles_inputField__3eqTj']")
    receipt_ingredients = (By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']")
    receipt_ingredients_count = (By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']")
    receipt_add_ingredient = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    receipt_cooking_duration = (By.XPATH, "(.//input[@class='styles_inputField__3eqTj'])[2]")
    receipt_desctiption = (By.XPATH, ".//textarea[@class='styles_textareaField__1wfhC']")
    receipt_create_button = (By.XPATH, ".//button[text()='Создать рецепт']")
    receipt_ingredients_list = (By.XPATH, "(.//div[@class='styles_container__3ukwm']/div[1])")
    receipt_upload_photo_button = (By.XPATH, ".//div[text()='Выбрать файл']")
    receipt_upload_photo_input = (By.XPATH, ".//input[@class='styles_fileInput__3HjP3']")


    # Receipt after creation
    receipt_card_after_creation = (By.XPATH, ".//h1[@class='styles_single-card__title__2QMPq']")
    receipt_name_after_creation = (By.XPATH, ".//img[@class='styles_single-card__image__O135K']")
    receipt_edit_button = (By.XPATH, ".//a[text()='Редактировать рецепт']")
    receipt_delete_button = (By.XPATH, ".//div[text()='Удалить']")