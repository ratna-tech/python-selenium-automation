from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

SELECT_PRODUCTS = (By.XPATH,"//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized']/li")
#PROD_NAME = (By.XPATH, "//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")
PROD_NAME = (By.XPATH,"//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized']//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")
TEXT_REG = (By.XPATH,"//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized']//descendant::span[6]")

@given('Open Wholefood page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz')

@then('name of product is present')
def verify_name_of_product(context):
    prod = context.driver.wait.until(EC.presence_of_all_elements_located(SELECT_PRODUCTS))
    prod_name = context.driver.wait.until(EC.presence_of_all_elements_located(PROD_NAME))

    for i in range(len(prod_name)):

        print(prod_name[i].text)
        assert prod_name[i].text != 0,f'Expected {prod_name[i].text} , but got nothing'


@then('text "Regular" is present')
def verify_text_Regular_present(context):
     text_regular = context.driver.wait.until(EC.presence_of_all_elements_located(TEXT_REG))
     for i in range(len(text_regular)):
         print(text_regular[i].text)
         assert 'Regular' in  text_regular[i].text , f'Expected Regular , but got {text_regular[i].text}'



