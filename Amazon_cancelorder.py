from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Ratna Sinha\Downloads\chromedriver_win32\Chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html/')

#search
search = driver.find_element(By.ID,'helpsearch')
search.clear()
search.send_keys('Cancel order')
#hit Enter
search.send_keys(Keys.ENTER)
# wait for 4 sec
sleep(4)


# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()