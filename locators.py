from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/User/Documents/Python Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice")
# driver.maximize_window()

#ID,Xpath,CSSSelector,ClassName,Name,linkText
#fill the email by using NAME attribute
driver.find_element(By.NAME,"email").send_keys("arunanaga99@gmail.com")
#fill the password by using id attribute
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID,"exampleCheck1").click()


#Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#for message
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

#for Name
#Css Selector - tagname[attribute='value'] ,#id,.classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("ARUNA")


assert "Success" in message

#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value
