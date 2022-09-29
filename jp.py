from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/User/Documents/Python Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.facebook.com/login")
driver.minimize_window()


