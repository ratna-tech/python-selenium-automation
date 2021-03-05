from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
class Cart_Page(Page):
  CART_LOCATOR = (By.ID, "nav-cart-count-container")
  CART_EMPTY_LOCATOR =(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

  #SELECT_PROD = (By.XPATH, "//span[@class='a-price-whole']//ancestor::a")



  def open_main_page(self):
      self.open_page('https://www.amazon.com/')

  def go_to_cart(self):
    self.click(*self.CART_LOCATOR)

  def verify_text_displays(self,verify_text ):
      self.verify_text(verify_text,*self.CART_EMPTY_LOCATOR)

