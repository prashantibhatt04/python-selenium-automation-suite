from pages.dynamic_loading_page import DynamicLoadingPage

class TestDynamicLoading:
    def test_finish_text_appears_after_loading(self, driver):
        page = DynamicLoadingPage(driver)
        page.load()
        page.click_start()
        assert "Hello World!" in page.get_finish_text()

    def test_finish_element_not_visible_before_start(self, driver):
        page = DynamicLoadingPage(driver)
        page.load()
        elements = driver.find_elements(
            __import__('selenium').webdriver.common.by.By.ID, "finish"
        )
        assert len(elements) == 0 or not elements[0].is_displayed()