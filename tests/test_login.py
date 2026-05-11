from pages.login_page import LoginPage

class TestLogin:
    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.load()
        page.enter_username("tomsmith")
        page.enter_password("SuperSecretPassword!")
        page.click_login()
        assert "You logged into a secure area!" in page.get_flash_message()

    def test_invalid_login(self, driver):
        page = LoginPage(driver)
        page.load()
        page.enter_username("wronguser")
        page.enter_password("wrongpass")
        page.click_login()
        assert "Your username is invalid!" in page.get_flash_message()

    def test_empty_credentials(self, driver):
        page = LoginPage(driver)
        page.load()
        page.click_login()
        assert "Your username is invalid!" in page.get_flash_message()