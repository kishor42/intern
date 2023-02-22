from selenium.webdriver.common.by import By

class Complete:
    def __init__(self, driver):
        self.driver = driver

    def backhome(self):
        b_home = self.driver.find_element(By.CSS_SELECTOR, 'button[id="back-to-products"]')
        b_home.click()
