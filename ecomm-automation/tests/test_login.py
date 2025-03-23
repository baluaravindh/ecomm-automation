import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/account/login")
    yield driver
    driver.quit()


def test_login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='r4vIwl BV+Dqf']")))
    username_field.send_keys("6281435933")

    req_otp_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Request OTP']")))
    req_otp_btn.click()

    assert "Online Shopping India | Buy Mobiles, Electronics, Appliances, Clothing and More Online at Flipkart.com" in driver.title
