from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new Chrome session
driver = webdriver.Chrome()

# Load your local HTML file
print("Opening login page...")
driver.get(r"file:///C:/Users/NEC/Desktop/AI%20Week%204%20Assignment/index.html")

# Give the browser a second to load
time.sleep(2)

# Interact with the page
print("Entering credentials...")
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")

print("Clicking login button...")
driver.find_element(By.ID, "loginBtn").click()

# Take a screenshot for your report
driver.save_screenshot("login_test_result.png")

print("✅ Test completed successfully!")

time.sleep(2)
driver.quit()
