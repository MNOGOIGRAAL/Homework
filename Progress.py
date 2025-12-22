import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'http://uitestingplayground.com/progressbar'

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(BASE_URL)
time.sleep(3)

start_button = driver.find_element(By.ID, value="startButton")
start_button.click()

while True:
    progress = driver.find_element(By.ID, value="progressBar")
    value = progress.get_attribute("aria-valuenow")
    if value >= "75":
        break

stop_button = driver.find_element(By.ID, "stopButton")
stop_button.click()
time.sleep(5)

driver.quit()