"""Page object for the DeviceProvisioning page. The ids are the contract the application must expose."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DeviceProvisioningPage:
    PATH = "/device-provisioning"
    FORM = (By.ID, "device-provisioning-form")
    SUBMIT = (By.ID, "submit")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, base_url):
        self.driver.get(base_url + self.PATH)
        return self

    def fill(self, field_id, value):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
        element.clear()
        element.send_keys(value)
        return self

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()
        return self

    def message(self):
        return self.wait.until(EC.visibility_of_element_located(self.MESSAGE)).text

    def title(self):
        return self.driver.title
