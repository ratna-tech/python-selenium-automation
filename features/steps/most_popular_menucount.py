from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.XPATH,"//a[@data-csa-c-slot-id='nav_cs_0']")
COUNT_MENU = (By.XPATH, "//div[@id='zg_tabs']/ul/li")
#RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='help-content']/h1")
#RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers menu')
def best_sellers(context):
    context.driver.find_element(*SEARCH_INPUT).click()
    sleep(4)


@then('count number of menu items with bestsellers')
def count_menu_icon(context):
    count = context.driver.find_elements(*COUNT_MENU)
    assert len(count) == 5
    sleep(1)


