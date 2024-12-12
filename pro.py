import time

from selenium import webdriver

from POM import HomePage


def test_search_buses():
    driver = webdriver.Chrome()
    driver.get("https://www.redbus.in/")
    driver.maximize_window()

    time.sleep(5)
    homepage = HomePage(driver)
    homepage.enter_source("Hyderabad")
    homepage.enter_destination("Bangalore")

    time.sleep(5)
    homepage.select_date("11")  # Pass the day you want to select, for example "10"
    time.sleep(5)
    homepage.click_search()
    time.sleep(10)


    driver.quit()

if __name__ == "__main__":
    test_search_buses()
