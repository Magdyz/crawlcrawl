from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# website to crawl

website = "https://duckduckgo.com/"
#https://www.royalmintven.com/our-coins

#PAth for webdriver

PATH = "C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(PATH)

#browser = webdriver.Chrome()

browser.get(website)

search = browser.find_element_by_id("search_form_input_homepage")
search.send_keys("royalmint gothic queen 2022")
search.send_keys(Keys.RETURN)
sleep(5)

# find an element to click using various options

#result = browser.find_element_by_id("r1-2")
#result.click()
try:
    result = browser.find_element_by_xpath("// a[contains(text(),\
    '2022')]").click()
except:
    print('Not Found')
sleep(15)

browser.quit()
#print(browser.title)
#time.delay(5)
#search = find_element_by_xpath("/html/body/div[5]/header/div/div/div/div/div[2]/div/form/div/input")
#search.send_keys("king")
#search.send_keys(Keys.RETURN)
