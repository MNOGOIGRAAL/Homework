import pytest

from auth import login, get_user
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, entrance",  [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True),
])
def test_auth(driver, username, password, entrance):
    driver.get("https://www.saucedemo.com/")

    input_username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    input_username.send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()

    result_URL = driver.current_url

    if entrance:
        assert "inventory.html" in result_URL, "Вход не выполнен"
    else:
        error = driver.find_element(By.XPATH, "//div[@class = 'error-message-container error']")
        assert error.is_displayed(), "Сообщение о блокировке не отобразилось"
