from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SELECT_LINKS = (By.XPATH,"//div[@id='zg_tabs']/ul/li")
LINK_PAGE_NAME = (By.XPATH,"//div[@id='zg_banner_text_wrapper']")


@given('Open amazon best sellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')

@then('name of link is present')
def verify_name_of_product(context):
    names = []
    LINKS = context.driver.wait.until(EC.presence_of_all_elements_located(SELECT_LINKS))

    for i in range(len(LINKS)):
      LINKS = context.driver.wait.until(EC.presence_of_all_elements_located(SELECT_LINKS))
      LINKS[i].click()
      context.page_name= context.driver.wait.until(EC.presence_of_element_located(LINK_PAGE_NAME))
      names.append(context.page_name.text)

    for name in names:
        assert 'Amazon Best Sellers' in names, f'Expected {"Amazon Best Sellers"} , but got {name}'
        assert 'Amazon Hot New Releases' in names, f'Expected {"Amazon Hot New Releases"} , but got {name}'
        assert 'Amazon Movers & Shakers' in names,f'Expected {"Amazon Movers & Shakers"} , but got {name}'
        assert 'Amazon Most Wished For'in names,f'Expected {"Amazon Most Wished For"} , but got {name}'
        assert 'Amazon Gift Ideas'in names,f'Expected {"Amazon Gift Ideas"} , but got {name}'

