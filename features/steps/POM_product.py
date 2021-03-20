from behave import given, when, then
from pages.product_page import ProductPage

VERIFY_TEXT = 'Your Amazon Cart is empty'
cart_item_num = '1'

@given('Open AmazonFirst page')
def open_amazon(context):
    context.app.carts_page.open_main_page()

@given('Open Amazon product page')
def open_amazon_product(context):
    context.app.product_page.open_product_page('gp/product/B074TBCSC8')

@when('Input {search_word} in searchbox')
def input_search(context, search_word):
  context.app.first_item_incart.input_search(search_word)


@when('click onthe search icon')
def click_search_icon(context):
    context.app.first_item_incart.click_search_icon()

@when('Select first1 {search_word} on the page')
def select_first1_item_in_page(context,search_word):
    context.app.product_page.select_first1_item_in_page()

@when('click on the Add to Cart button')
def add_item_to_cart(context):
    context.app.product_page.add_item_to_cart()



@then('number of the items added in the cart is displayed')
def verify_item_incart(context):
    context.app.product_page.verify_item_incart()

@when('Hover Over New Arrivals')
def hover_newarrivals(context):
    context.app.product_page.hover_over()


@then('verify deals is shown')
def verify_dealsdisplayed_onhover(context):
    context.app.product_page.deals_whenhover_displayed()

