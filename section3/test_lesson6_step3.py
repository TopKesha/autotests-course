import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_right_answer(browser, number):
    
    browser.implicitly_wait(3)
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answ = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea")))
    answer = str(math.log(int(time.time()+1)))
    answ.send_keys(answer)

    button = browser.find_element_by_css_selector ("button.submit-submission")
    button.click()

    got = browser.find_element_by_css_selector (".smart-hints__hint")

    assert "Correct!" in got.text, f"Failed: expected Correct!, got {got.text}" 
