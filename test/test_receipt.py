import allure


class TestReceipt:

    @allure.title('Создание нового рецепта')
    def test_create_new_receipt_positive(self, profile_auth, receipt):
        receipt.click_on_create_receipt_header()
        receipt.fill_the_entire_receipt_form()
        
        assert receipt.check_create_receipt_card_success()
        assert receipt.check_create_receipt_name_success()