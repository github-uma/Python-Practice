import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Start writing python codes below")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name('q')
search_bar.clear()
search_bar.send_keys("getting started with python")
time.sleep(10)
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()