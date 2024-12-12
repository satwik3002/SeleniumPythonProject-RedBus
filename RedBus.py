import pytest
selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Step 2: Enter current date and search buses
    wait.until(EC.presence_of_element_located((By.ID, "src"))).send_keys("Hyderabad")
    wait.until(EC.presence_of_element_located((By.ID, "dest"))).send_keys("Bangalore")
    driver.find_element(By.ID, f"//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 fgdqFw' and text()='{"11"}]").click()

    driver.find_element(By.ID, "search_btn").click()

    # Step 4: Click on Modify button
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modify-btn"))).click()

    # Step 5: Select a date 7 days later
    driver.find_element(By.ID, "onward_cal").click()
    date_xpath = f"//td[text()='{int(time.strftime('%d')) + 7}']"
    wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath))).click()
    driver.find_element(By.ID, "search_btn").click()

    # Step 7: Scroll to the 6th Primo bus and click 'View Seats'
    primo_buses = driver.find_elements(By.CLASS_NAME, "bus-items")
    if len(primo_buses) >= 6:
        actions = ActionChains(driver)
        actions.move_to_element(primo_buses[5]).perform()
        primo_buses[5].find_element(By.XPATH, ".//button[text()='View Seats']").click()

    # Step 9: Select any seat in the upper berth
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "upper-berth"))).click()

    # Step 10: Select boarding and dropping points
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Hebbal']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Miyapur']"))).click()

    # Step 12: Scroll down and view prices for any bus
    actions.move_to_element(driver.find_element(By.CLASS_NAME, "fare-section"))
    actions.perform()
    driver.find_element(By.XPATH, "//button[text()='View Prices']").click()

finally:
    # Exit the browser
    time.sleep(5)
    driver.quit()
