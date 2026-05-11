from pages.checkboxes_page import CheckboxesPage

class TestCheckboxes:
    def test_first_checkbox_unchecked_by_default(self, driver):
        page = CheckboxesPage(driver)
        page.load()
        assert page.is_checked(0) == False

    def test_second_checkbox_checked_by_default(self, driver):
        page = CheckboxesPage(driver)
        page.load()
        assert page.is_checked(1) == True

    def test_can_check_first_checkbox(self, driver):
        page = CheckboxesPage(driver)
        page.load()
        page.click_checkbox(0)
        assert page.is_checked(0) == True