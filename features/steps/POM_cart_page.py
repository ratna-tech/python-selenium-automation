from behave import given, when, then


VERIFY_TEXT = 'Your Amazon Cart is empty'
cart_item_num = '1'

@given('Open Amazon_main page')

def open_amazon(context):
    context.app.carts_page.open_main_page()

@when('Click on cart icon')
def go_to_cart(context):
    context.app.carts_page.go_to_cart()

@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_text_displays(context):
    context.app.carts_page.verify_text_displays(VERIFY_TEXT)

