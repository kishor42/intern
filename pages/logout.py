from selenium.webdriver.common.by import By

class Logout:
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        c_menu = self.driver.find_element(By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
        c_menu.click()

    def page_logout(self):
        p_logout = self.driver.find_element(By.CSS_SELECTOR, ' a[id="logout_sidebar_link"]')
        p_logout.click()

