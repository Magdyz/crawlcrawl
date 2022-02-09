from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('https://www.royalmint.com/our-coins')
print(browser.title)
time.delay(5)
search = find_element_by_xpath("/html/body/div[5]/header/div/div/div/div/div[2]/div/form/div/input")
search.send_keys("king")
search.send_keys(Keys.RETURN)
