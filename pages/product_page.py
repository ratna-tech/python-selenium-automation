from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(Page):

  SELECT_PROD = (By.XPATH, "//span[@class='a-price-symbol']//ancestor::a")
  #SELECT_PROD = (By.XPATH, "//div[@data-deal='LIGHTNING_DEAL']")
  ADD_CART = (By.ID, 'add-to-cart-button')
  OPEN_CART = (By.ID, "nav-orders")
  CHECK_CART = (By.ID, 'nav-cart-count')
  cart_item_num = '1'
  SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
  SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
  NEW_ARRIVAL = (By.XPATH,'//div[@id ="nav-subnav"]//child::a[7]//child::span[1]')
  DEALS_POPUP = (By.ID, "//div[@id='nav-flyout-aj:https://softlines-trova.s3-us-west-2.amazonaws.com/prod/US/mediaservice/megamenucreator_basic_en_US.json:subnav-sl-megamenu-8:0']")
  DEAL_POP = (By.XPATH, "//div//a[@class='mm-merch-panel']//child::ul//li[2][text()='See More']")
  APPLIANCE_Disp = (By.ID,"//span[@id='nav-search-label-id']")
  APP_DISP = (By.ID,"nav-search-label-id")
  DEALS =(By.XPATH,"//div[@class='mega-menu']")

  def open_main_page(self):
    self.open_page( )

  def open_product_page(self, url=''):
    self.open_page(url)

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

  def hover_over(self):
    item_tab =self.find_element(*self.NEW_ARRIVAL)
    actions = ActionChains(self.driver)
    actions.move_to_element(item_tab)
    actions.perform()
    from time import sleep
    sleep(5)

  def deals_whenhover_displayed(self):
    self.find_element(*self.DEAL_POP)
   # self.find_element(*self.APP_DISP)

  def verify_dept_displayed(self, DEPT_NAME):
    #self.verify_text(*self.DEPT_NAME,*self.APP_DISP)
    dept=self.find_element(*self.APP_DISP)
    dept_name = dept.text
    assert dept_name==DEPT_NAME, f'Expected {DEPT_NAME} but got {dept_name}'
