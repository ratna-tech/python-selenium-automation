from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

VERIFY_TEXT = 'Sign-In'

@given('Open Amazonmain page')
def open_amazon(context):
    context.app.main_page.open_main_page()

@when('Click Amazon Orders link')
def go_to_orders(context):
    context.app.main_page.Click_Amazon_Orders_link()

@then("Verify Sign In page is opened")
def verify_page_opens(context):
    context.app.main_page.Verify_Sign_In(VERIFY_TEXT)

