import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

#radio buttons won't change
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


#is_displayed method
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").is_displayed()
#assert not driver.find_element(By.ID,"displayed-text").is_displayed()

