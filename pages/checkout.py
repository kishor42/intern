from selenium.webdriver.common.by import By

class CheckOut:
    def __init__(self, driver):
        self.driver = driver


    def first_name(self):
        f_name = self.driver.find_element(By.CSS_SELECTOR,'input[id="first-name"]')
        f_name.send_keys("kishor")



    def last_name(self):
        l_name = self.driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
        l_name.send_keys("kandel")



    def zip_code(self):
        z_code = self.driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')
        z_code.send_keys("125")

    def checkout_continue(self):
        c_continue = self.driver.find_element(By.CSS_SELECTOR, 'input[id="continue"]')
        c_continue.click()


