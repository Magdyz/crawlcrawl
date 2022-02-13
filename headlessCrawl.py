from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, os, difflib
from pathlib import Path

############## THREE THINGS TO CHANGE BEFORE YOU START
#############  WEBSITE - the website to fetch html from
###########    folderPathWithoutFile - the path where the html file will be exported to
#########      PATH - the path to the webdriver in my case chrome driver

# Website to crawl by an input from user (will add sanitisation for input)
userAddedWebsite = input('Please type website name:\n')
website = "https://" + userAddedWebsite

# for testing purposes
#website = 'https://www.example.com'

##### add a confirmation with a yes and no to proceed or change name ######

## Paths for files to go in the same folder as the program.

folderPathWithoutFile = os.path.dirname(os.path.abspath(sys.argv[0]))+'\\'
differencesFile = folderPathWithoutFile+'differences.txt'

#Before starting clear the differences file in order to start a fresh
if os.path.exists(differencesFile):
    os.remove(differencesFile)
    print('Removed differences file to create new one!')
    
else:
    for i in range(5):
        print(".") 


# The default naming and path for export file to be saved
# folderPathWithoutFile needs to be changed 
# to where you want to save file
    
#folderPathWithoutFile = 'C:\\Users\magdy\Documents\my_Code\openWeb\websiteScheduler\crawlcrawl\\'

name = 'file'
num = 1
ext = '.txt'
file = name+str(num)+ext
print(file+ ' will be put in the following path:\n'+folderPathWithoutFile)

# check folder to make sure there are no duplicates and 
# create new name

while True:
    folderPath = folderPathWithoutFile+file
    fileExists = os.path.exists(folderPath)
    if fileExists:
        print(f"{file} name exists, we'll have to change it")
        num+=1
        file = name+str(num)+ext
        print(f" This is the new file name: {file}")
        continue
    else:
        file = name+str(num)+ext
        print("File name looks good!")
        break

#Path for browser webdriver and user agent

PATH = "C:\Program Files/chromedriver.exe"
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
    with open(folderPath, 'wt', encoding='utf-8') as newFile:
        newFile.write(html)
    print(f'Exported {file} to {folderPath} successfully')
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

#old file with previous verison of the website's html


try:
    oldFile = name+str(num-1)+ext
    oldFilePath = folderPathWithoutFile+oldFile
    print(oldFile+' vs '+file)

    with open(oldFilePath, encoding="utf8") as file_1:
        file_1_text = file_1.readlines()
    
    with open(folderPath, encoding="utf8") as file_2:
        file_2_text = file_2.readlines()
    
    # Find and print the diff:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile=oldFile, 
            tofile=file, lineterm=''):
            #print(line)
            with open(differencesFile, 'a', encoding='utf-8') as newFileCompare:
                newFileCompare.write(line+'\n')
    print(f'The differences have been successfully written to {differencesFile}')
except:
    print('No old file to compare with')
