from identitycrisis import firstname, lastname, agenumber, passwordgen, username
from selenium import webdriver

account = firstname, lastname, username, passwordgen
jump = "\n"
saveFile = open('accounts', 'a')
saveFile.write(str(account) + "\n")
saveFile.close()


driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-n-en&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.find_element_by_id('firstName').send_keys(firstname)
driver.find_element_by_id('lastName').send_keys(lastname)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_name('Passwd').send_keys(passwordgen)
driver.find_element_by_name('ConfirmPasswd').send_keys(passwordgen)
driver.find_element_by_class_name('CwaK9').click()
driver.find_element_by_id('#phoneNumberId.whsOnd.zHQkBf').send_keys("4135578153")
driver.find_element_by_class_name('CwaK9').click()
