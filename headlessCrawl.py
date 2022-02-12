from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# Website to crawl

website = "https://egypt.gov.eg/english/guide/directory.aspx"

#https://www.royalmintven.com/our-coins

# The default naming and path for export file to be saved
# folderPathWithoutFile needs to be changed 
# to where you want to save file
    
folderPathWithoutFile = "C:/Users/Magdy/Documents/webDev/crawlcrawl/headlessCrawl/"
name = 'file'
num = 1
ext = '.txt'
file = name+str(num)+ext
print(file)

# check folder to make sure there are no duplicates and 
# create new name

while True:
    folderPath = folderPathWithoutFile+file
    fileExists = os.path.exists(folderPath)
    if fileExists:
        num+=1
        file = name+str(num)+ext
        print(file)
        continue
    else:
        break

#Path for browser webdriver and user agent

PATH = "C:\Program Files\chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

#Headless chrome webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=PATH, options=options)

# Get website and write html to file in same folder.

try:
    driver.get(website)
    html = driver.page_source
    with open(file, 'wt', encoding='utf-8') as newFile:
        newFile.write(html)
    print('success')
except:
    print('Not Found')

driver.quit()
print('closed')

#sleep(15)
#print(html)

# if you want to add a screenshot remove hashtag 
#driver.get_screenshot_as_file('file.png')

#if you want browser to wait until loaded completely
#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"ptifrmtgtframe")))

#if you want to print page source
#print(driver.page_source)



