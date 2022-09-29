from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "aruna"

service_obj = Service("D:/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

#switch from driver to alert mode bcs driver is not aware of alert so
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText

# accept is the method to click on alert dialogue box
alert.accept() #for clicking ok
#alert.dismiss()
