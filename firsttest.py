
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome()
driver.get("http://mail.ru")
element = driver.find_element_by_name("login")
element.send_keys("9629460714")
element.send_keys(Keys.RETURN)
felement = driver.find_element_by_name("password")
#felement.send_keys("")
felement.send_keys(Keys.RETURN)
driver.title
if driver.title == "Входящие - Почта Mail.ru":
    selement = driver.find_element_by_xpath("//input[@class ='b-toolbar__btn js-shortcut']")
    driver.get("http://e.mail.ru" + selement.get_attribute("href"))
    selement.click()
  
else: 
    print ("ошибка")
driver.close()