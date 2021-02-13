from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID,'helpsearch')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='help-content']/h1")
#RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon cancel order page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/')


@when('Input {search_word} into search box')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Tap on Enter key')
def Tap_search_icon(context):
    tap = context.driver.find_element(*SEARCH_INPUT)
    tap.send_keys(Keys.ENTER)
    sleep(1)


@then('Page for {search_word} is displayed')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


