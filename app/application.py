from pages.main_page import Main_Page
from pages.carts_page import Cart_Page
from pages.first_item_incart import FirstItem_Cart
class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main_Page(self.driver)
        self.carts_page = Cart_Page(self.driver)
        self.first_item_incart  = FirstItem_Cart(self.driver)