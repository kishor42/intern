from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Product:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_backpack(self):
        to_cart_backpack = self.driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-backpack"]')
        to_cart_backpack.click()


    def add_to_cart_bike_light(self):
        to_cart_bike_light = self.driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-bike-light"]')
        to_cart_bike_light.click()

    def add_to_cart_bolt_tshirt(self):
        to_cart_tshirt = self.driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        to_cart_tshirt.click()


    def add_to_cart_fleece_jacket(self):
        to_cart_fleece_jacket = self.driver.find_element(By.CSS_SELECTOR,'button[id="add-to-cart-sauce-labs-fleece-jacket"]')
        to_cart_fleece_jacket.click()


