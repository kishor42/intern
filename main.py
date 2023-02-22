from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from pages.Login import Login
from pages.Product import Product
from pages.yourcart import YourCart
from pages.checkout import CheckOut
from pages.checkoutdescription import CheckOutDescription
from pages.complete import Complete
from pages.logout import Logout

import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

login_page = Login(driver)
driver.get("https://www.saucedemo.com/")
login_page.set_username("standard_user")
login_page.set_password("secret_sauce")
login_page.click_login()


product_page = Product(driver)
product_page.add_to_cart_backpack()
product_page.add_to_cart_bike_light()
product_page.add_to_cart_bolt_tshirt()
time.sleep(1)


cart = YourCart(driver)
cart.remove_backpack()
time.sleep(1)
cart.go_to_cart()
time.sleep(1)
cart.shop()
time.sleep(1)


product_page.add_to_cart_fleece_jacket()
time.sleep(1)

cart.go_to_cart()
time.sleep(1)

cart.checkout()
time.sleep(5)

cout = CheckOut(driver)
cout.first_name()
cout.last_name()
cout.zip_code()
cout.checkout_continue()
time.sleep(3)

cod = CheckOutDescription(driver)
cod.cod_finish()
time.sleep(2)

comp = Complete(driver)
comp.backhome()
time.sleep(2)

log = Logout(driver)
log.click_menu()
log.click_menu()
time.sleep(5)
