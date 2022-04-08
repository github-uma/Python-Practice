import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\umayadav\\Desktop\\Automation\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(5) # wait for 5 seconds
print(driver.current_url)
driver.get("https://www.bhaskar.com/db-original/news/india-stand-in-russia-ukraine-war-129554019.html")
time.sleep(5) # wait for 5 seconds
print(driver.title)
driver.back()
driver.refresh()
time.sleep(5) # wait for 5 seconds
driver.close()
