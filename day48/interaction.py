from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# element = driver.find_element(By.CSS_SELECTOR, 'a[title="Special:Statistics"]')
# element = driver.find_element(By.LINK_TEXT,value="Content portals")
# element.click()

# find search abr and type
fname = driver.find_element(By.NAME,value="fName")
fname.send_keys("mayank")

lname = driver.find_element(By.NAME,value="lName")
lname.send_keys("mehta")

email = driver.find_element(By.NAME,value="email")
email.send_keys("mayank@123gmail.com")

button = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
button.send_keys(Keys.ENTER)







# driver.quit()