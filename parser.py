# Мы использовали библиотеку selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, desired_capabilities=caps)

driver.get('https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/Rail_Insurance_Claims.csv')
time.sleep(1)

with open('dataset.csv', 'w') as f:
    f.write(driver.find_element(By.TAG_NAME, value='body').text)
