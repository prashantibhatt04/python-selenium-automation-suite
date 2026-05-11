from selenium.webdriver.common.by import By
import os

class UploadPage:
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def upload_file(self, filename):
        file_path = os.path.abspath(filename)
        self.driver.find_element(By.ID, "file-upload").send_keys(file_path)
        self.driver.find_element(By.ID, "file-submit").click()

    def get_uploaded_filename(self):
        return self.driver.find_element(By.ID, "uploaded-files").text