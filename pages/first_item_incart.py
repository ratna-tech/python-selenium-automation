from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstItem_Cart(Page):

  SELECT_PROD = (By.XPATH, "//span[@class='a-price-symbol']//ancestor::a")
  #SELECT_PROD = (By.XPATH, "//div[@data-deal='LIGHTNING_DEAL']")
  ADD_CART = (By.ID, 'add-to-cart-button')
  OPEN_CART = (By.ID, "nav-orders")
  CHECK_CART = (By.ID, 'nav-cart-count')
  cart_item_num = '1'
  SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
  SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')

  def open_main_page(self):
    self.open_page('https://www.amazon.com/')

  def input_search(self,search_word):
    search =self.driver.find_element(*self.SEARCH_INPUT)
    search.send_keys(search_word)

  def click_search_icon(self):
    self.driver.find_element(*self.SEARCH_SUBMIT).click()

  def select_first1_item_in_page(self):
    self.driver.find_element(*self.SELECT_PROD).click()

  def add_item_to_cart(self):
    self.driver.find_element(*self.ADD_CART).click()

  def verify_item_incart(self):
    self.verify_text(*self.cart_item_num, *self.CHECK_CART)




