import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.from_input_locator = "//input[@id='src']"
        self.to_input_locator = "//input[@id='dest']"
        self.date_picker_locator = "//input[@id='onward_cal']"
        self.search_button_locator = "//button[@id='search_button']"

    def enter_source(self, source):
        self.driver.find_element(By.XPATH, self.from_input_locator).send_keys(source)
        time.sleep(2)
        highlighted_option_locator = "//li[contains(@class, 'sc-iwsKbI') and contains(@class, 'cursorPointing')]"
        highlighted_option = self.driver.find_element(By.XPATH, highlighted_option_locator)
        highlighted_option.click()

    def enter_destination(self, destination):
        self.driver.find_element(By.XPATH, self.to_input_locator).send_keys(destination)
        time.sleep(2)
        highlighted_option_locator = "//li[contains(@class, 'sc-iwsKbI') and contains(@class, 'cursorPointing')]"
        highlighted_option = self.driver.find_element(By.XPATH, highlighted_option_locator)
        highlighted_option.click()

    def select_date(self, date):
        date_picker = self.driver.find_element(By.ID, "onwardCal")
        date_picker.click()
        time.sleep(2)
        day_locator = f"//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 fgdqFw' and text()='{date}']"
        day_element = self.driver.find_element(By.XPATH, day_locator)
        day_element.click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.search_button_locator).click()
