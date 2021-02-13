from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.common.exceptions import NoSuchElementException
ele_text =[]
topics = []
elements = []
HEADER_UI = (By.XPATH, '//div[@class="a-section a-spacing-extra-large a-spacing-top-extra-large ss-landing-container"]/h1')
ELEMENTS_PRESENT = (By.XPATH, "//div[@class='a-box self-service-rich-card']")
ELEMENTS_TEXT = (By.XPATH, "//div[@class='a-box self-service-rich-card']//h3[@class='a-spacing-none a-text-normal']")
RESULTS = (By.XPATH, "//div[@class='g']")
ELEMENT_TEXT =(By.XPATH, "//div[@class='a-box self-service-rich-card']//span[@class='a-list-item a-color-secondary']")
TEXT_BOX = (By.ID,"helpsearch")
HEADING_PRESENT = (By.XPATH, "//div[@class='a-span12 a-column a-spacing-top-small']/h1")
LIST_PRESENT = (By.XPATH,"//li[@class='csg-category']")

@given('Open Amazon customer help page')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('text for Customer help is displayed')
def verify_Heading_text(context):
    Heading = context.driver.find_element(*HEADER_UI).text
    assert Heading == "Hello. What can we help you with?"

@then('elements for somethings you can do here count')
def verify_elements_count(context):
    elements = context.driver.find_elements(*ELEMENTS_PRESENT)
    assert len(elements) == 8
    print(len(elements))

@then('elements text is present')
def verify_elements_present(context):
    elements = context.driver.find_elements(*ELEMENTS_TEXT)
    for i in range(len(elements)):
        print(elements[i].text)

@then('verify search the help library textbox')
def verify_textbox_present(context):
    try:
      context.driver.find_element(*TEXT_BOX)

      print("textbox exist" )
# NoSuchElementException thrown if not present
    except NoSuchElementException:
     print("textbox does not exist")

@then('Browse Help Topics heading present')
def verify_heading(context):
    heading = context.driver.find_element(*HEADING_PRESENT).text
    assert heading  == "Browse Help Topics"

@then('recommeneded topics present')
def verify_topic_list(context):
    topics = context.driver.find_elements(*LIST_PRESENT)
    assert len(topics)  == 12
    for i in range(len(topics)):
        print(topics[i].text)