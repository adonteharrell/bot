from identitycrisis import firstname, lastname, agenumber, passwordgen, username
from selenium import webdriver

account = firstname, lastname, username, passwordgen
jump = "\n"
saveFile = open('accounts', 'a')
saveFile.write(str(account) + "\n")
saveFile.close()


driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-n-en&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.find_element_by_name('text').send_keys(username + "@gmail.com")
driver.find_element_by_class_name('signinForm__cta signinForm__checkIdentifierCTA sc-button-cta sc-button sc-button-large').click()
driver.find_element_by_id('formControl_688').send_keys(passwordgen)
driver.find_element_by_class_name('recaptcha-checkbox-checkmark').click()
driver.find_element_by_id('recaptcha-audio-button').click()


