from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Hot-Wheels-Cars-Gift-Styles/dp/B01BMW645O")

try:
    # Wait until the price element is visible (max 10 seconds)
    price_dollar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
    print(f"The price is {price_dollar.text}.{price_cents.text}")

except Exception as e:
    print("Error:", e)

driver.quit() # Only close if you want to shut the browser
