from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class Main_Page(Page):
  ORDER_LOCATOR = (By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
  SIGNIN_LOCATOR =(By.XPATH,"//h1[@class='a-spacing-small']")
  #SELECT_DROPDOWN = (By.ID,"//select[@id='searchDropdownBox']")
  SELECT_DROPDOWN = (By.CSS_SELECTOR,'select.nav-search-dropdown')
  INPUT_TEXT= (By.ID,'twotabsearchtextbox')
  SEARCH_ICON = (By.ID,"nav-search-submit-button")

  def open_main_page(self):
      self.open_page('')

  def Click_Amazon_Orders_link(self):
    self.click(*self.ORDER_LOCATOR)

  def Verify_Sign_In(self,verify_text ):
      self.verify_text(verify_text,*self.SIGNIN_LOCATOR)

  def select_department(self,alias:str):
      #dd = self.find_element(*self.SELECT_DROPDOWN)
      print(alias)
      select = Select(self.find_element(*self.SELECT_DROPDOWN))
      select.select_by_value(f'search-alias={alias}')


  def search_prod(self,search_word):
      self.input_text(search_word,*self.INPUT_TEXT)
      #search = self.find_element(*self.INPUT_TEXT)
      #search.clear()
      #search.send_keys(search_word)
      self.click(*self.SEARCH_ICON)



