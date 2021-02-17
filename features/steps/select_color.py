from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

SELECT_SIZEDROPBOX = (By.XPATH,"//a[@class='a-dropdown-link a-active']")
SELECT_SIZE = (By.ID, 'size_name_0')
SELECT_COLOR = (By.XPATH,"//div[@class='tooltip']")
COLOR_TEXT = (By.XPATH, "//div[@class='a-row']//span[@class='selection']")
#RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon product B07BJKRR25 page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


#@when('select size')
#def select_size(context):
   # dropdown  = context.driver.wait.until(EC.presence_of_element_located(SELECT_SIZEDROPBOX))
  #  dropdown.click()
  #  size = context.driver.wait.until(EC.presence_of_element_located(SELECT_SIZE))
  #  size.click()

#context.driver.wait.until((EC.element_to_be_clicable(By.  )))
@when('select color')
def select_color(context):
    expected_colors =['Black','Blue Overdyed','Dark Vintage','Dark Wash','Indigo Wash','Light Vintage',
                      'Light Wash','Medium Vintage','Medium Wash','Rinse','Rinsed Vintage','Vintage Light Wash'
                      ,'Washed Black']
    color = context.driver.wait.until(EC.presence_of_all_elements_located(SELECT_COLOR))
    for i in range(len(color)):
        color[i].click()
        color_text = context.driver.wait.until(EC.presence_of_element_located(COLOR_TEXT)).text
        print(color_text)
        print(expected_colors[i])
        assert expected_colors[i]== color_text, f'Expected {expected_colors[i]} , but got {color_text}'


#@then('text for color changes according to the color election')
#def verify_color_get_selected(context):


