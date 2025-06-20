from selenium import webdriver

#Launch Chrome
driver = webdriver.Chrome()

#Open Facebook
driver.get('https://www.facebook.com')

#find Elements by their Traditional Locators
driver.find_element("id", "email").send_keys("Your_Email_ID")
driver.find_element("id","pass").send_keys("Your_Password")
driver.find_element("name", "login").click()

driver.implicitly_wait(5) # this will open faceboom page and wait for 10 seconds


driver.quit()  # this will close the facebook page after 10 seconds


