from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://github.com/shaantanu9')
while True:
    time.sleep(0)
    driver.refresh()
driver.quit()