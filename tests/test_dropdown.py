from pages.dropdown_page import DropdownPage

class TestDropdown:
    def test_select_option_1(self, driver):
        page = DropdownPage(driver)
        page.load()
        page.select_by_visible_text("Option 1")
        assert page.get_selected_option() == "Option 1"

    def test_select_option_2(self, driver):
        page = DropdownPage(driver)
        page.load()
        page.select_by_visible_text("Option 2")
        assert page.get_selected_option() == "Option 2"