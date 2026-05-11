from selenium.webdriver.common.by import By

class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    def is_checked(self, index):
        return self.get_checkboxes()[index].is_selected()

    def click_checkbox(self, index):
        self.get_checkboxes()[index].click()