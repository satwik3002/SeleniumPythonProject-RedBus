import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://www.redbus.in/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "src").send_keys('Bangalore')
time.sleep(2)
driver.find_element(By.ID, "dest").send_keys('Hyderabad')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="onwardCal"]/div/i').click()
time.sleep(2)
driver.find_element(By.XPATH, f"//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 fgdqFw' and text()='{11}']").click()
time.sleep(2)
driver.find_element(By.ID,"search_button").click()
time.sleep(10)
driver.find_element(By.XPATH,"//div[contains(text(),'Modify')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='11-Dec-2024']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='18']").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="fixer"]/section/div/div[4]/button').click()
time.sleep(20)
driver.execute_script("window.scrollBy(0, 2500);")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"li[id='27093543'] div[class='button view-seats fr']").click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="rt_31584617"]/div/div/div/div[3]/div[2]/div[3]/canvas').click()
time.sleep(5)