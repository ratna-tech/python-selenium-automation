from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
DEPT_NAME = 'Appliances'

#@given('Open Amazon cancel order page')
#def open_amazon(context):
    #context.driver.get('https://www.amazon.com/gp/help/customer/display.html/')
    #context.app.order_cancel.open_order_page()
#    pass

@when('select department by alias {alias}')
def select_app_dept(context,alias):
    #search = context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    #search.send_keys(search_word)
    context.app.main_page.select_department(alias)
    sleep(4)


@when('search for {search_word}')
def search_blenders(context,search_word):
    #tap = context.driver.find_element(*SEARCH_INPUT)
    #tap.send_keys(Keys.ENTER)
    context.app.main_page.search_prod(search_word)



@then('verify Appliances department is selected')
def department_disp(context):
    context.app.product_page.verify_dept_displayed(DEPT_NAME)