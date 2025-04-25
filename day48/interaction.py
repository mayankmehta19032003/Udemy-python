from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.CSS_SELECTOR, 'a[title="Special:Statistics"]')
print(element.text)




driver.quit()