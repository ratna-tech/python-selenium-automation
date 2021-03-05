from behave import given, when, then
from pages.first_item_incart import FirstItem_Cart

VERIFY_TEXT = 'Your Amazon Cart is empty'
cart_item_num = '1'

@given('Open AmazonFirst page')
def open_amazon(context):
    context.app.carts_page.open_main_page()

@when('Input {search_word} in searchbox')
def input_search(context, search_word):
  context.app.first_item_incart.input_search(search_word)


@when('click onthe search icon')
def click_search_icon(context):
    context.app.first_item_incart.click_search_icon()

@when('Select first1 {search_word} on the page')
def select_first1_item_in_page(context,search_word):
    context.app.first_item_incart.select_first1_item_in_page()

@when('click on the Add to Cart button')
def add_item_to_cart(context):
    context.app.first_item_incart.add_item_to_cart()



@then('number of the items added in the cart is displayed')
def verify_item_incart(context):
    context.app.first_item_incart.verify_item_incart()
