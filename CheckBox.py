from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    #checkbox arrangement will change so we have to check
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        # to know checkbox is selected or not by using selenium method
        assert checkbox.is_selected()
        break

