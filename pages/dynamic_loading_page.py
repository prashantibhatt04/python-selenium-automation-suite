from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoadingPage:
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def click_start(self):
        self.driver.find_element(By.CSS_SELECTOR, "#start button").click()

    def get_finish_text(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        return element.text