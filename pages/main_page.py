from selenium.webdriver.common.by import By
from pages.base_page import Page

class Main_Page(Page):
  ORDER_LOCATOR = (By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
  SIGNIN_LOCATOR =(By.XPATH,"//h1[@class='a-spacing-small']")


  def open_main_page(self):
      self.open_page('https://www.amazon.com/')

  def Click_Amazon_Orders_link(self):
    self.click(*self.ORDER_LOCATOR)

  def Verify_Sign_In(self,verify_text ):
      self.verify_text(verify_text,*self.SIGNIN_LOCATOR)