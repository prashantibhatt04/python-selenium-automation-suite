from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def select_by_visible_text(self, text):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text(text)

    def get_selected_option(self):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        return dropdown.first_selected_option.text