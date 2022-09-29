from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/User/Documents/Python Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://www.instagram.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME,"username").send_keys("arunanaga99@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Aruna@877679")
driver.find_element(By.XPATH,"//button[(@type='submit')]").click()

# driver.minimize_window()
# driver.refresh()
# driver.close()

