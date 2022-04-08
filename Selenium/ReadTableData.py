import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://qavbox.github.io/demo/webtable/")
driver.implicitly_wait(30)
table = driver.find_element(By.ID, "table01")
rows = table.find_elements(By.XPATH, "tbody/tr")
print("rows - " + str(len(rows)))
for i in range(len(rows)):
    columns = rows[i].find_elements(By.XPATH, "td")
    print("columns - " + str(len(columns)))
    for j in range(len(columns)):
        print(columns[j].text)
time.sleep(5)