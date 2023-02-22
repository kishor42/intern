from selenium.webdriver.common.by import By

class CheckOutDescription:
    def __init__(self, driver):
        self.driver = driver

    def cod_finish(self):
        c_finish = self.driver.find_element(By.CSS_SELECTOR, 'button[id="finish"]')
        c_finish.click()

    def cod_cancel(self):
        Cod_cancel = self.driver.find_element(By.CSS_SELECTOR, 'button[id="cancel"]')
        Cod_cancel.click()
