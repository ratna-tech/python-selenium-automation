from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
SELECT_PROD = (By.XPATH, "//span[@class='a-price-whole']//ancestor::a")
ADD_CART =(By.ID,'add-to-cart-button')
OPEN_CART = (By.ID, "nav-orders")
CHECK_CART = (By.ID,'nav-cart-count')



@when('Input {search_word} into search')
def input_search(context, search_word):
    search =context.driver.find_element(*SEARCH_INPUT)
    search.send_keys(search_word)


@when('click on the search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@when('Select first {search_word} on page')
def select_first_item_in_page(context, search_word):
    context.driver.find_element(*SELECT_PROD).click()


@when('click on Add to Cart button')
def add_item_to_cart(context):
    context.driver.find_element(*ADD_CART).click()
    sleep(3)


@then('number of items added in the cart is displayed')
def verify_item_incart(context):
    cart_item_num = context.driver.find_element(*CHECK_CART).text
    print(cart_item_num)
    assert int(cart_item_num) == 1