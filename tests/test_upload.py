from pages.upload_page import UploadPage

class TestUpload:
    def test_file_upload_success(self, driver):
        page = UploadPage(driver)
        page.load()
        page.upload_file("test_upload.txt")
        assert "test_upload.txt" in page.get_uploaded_filename()