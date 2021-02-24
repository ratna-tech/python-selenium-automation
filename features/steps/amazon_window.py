from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.LINK_TEXT,'Amazon applications')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_TEXT = (By.XPATH, "//p[@id='mgt-email-sms-download-header']")
#RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    all_window = context.driver.window_handles


@when("Click on Amazon applications link")
def click_app_link(context):
    context.driver.find_element(*SEARCH_INPUT).click()


@when('Switch to the newly opened window')
def click_app_link(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(context.driver.window_handles[1])

@then('Amazon app page is opened')
def verify_in_new_window(context):
   results_text = context.driver.find_element(*RESULTS_FOUND_TEXT).text
   expected_text='Download the app today!'
   assert expected_text in results_text, "Expected word '{}' in message, but got '{}'".format(expected_text, results_text)

@then('User can close new window and switch back to original')
def verify_open_original_win(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)