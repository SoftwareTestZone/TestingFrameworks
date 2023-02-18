from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import utilities.config


# /Users/shorya/.jenkins/secrets/initialAdminPassword
# b7d899b121f64f6db8b6dc228920a1b7 - Jenkins Passcode
# This may also be found at: /Users/shorya/.jenkins/secrets/initialAdminPassword

chromeDriver = webdriver.Chrome() 


def openWebDriver():
    return webdriver.Chrome()

def navigateLink(url):
    return chromeDriver.get(url)

def isElementVisible(element):
    try:
        wait = WebDriverWait(driver=chromeDriver, timeout= utilities.config.maximumTimeout)
        wait.until(expected_conditions.element_located_to_be_selected(By.CSS_SELECTOR, element))
    except Exception as e:
        print ("Exception is:- ", e)

def isElementVisibleAndClickable(element):
    try:
        wait = WebDriverWait(driver=chromeDriver, timeout=utilities.config.maximumTimeout)
        wait.until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR, element)).click()
    except Exception as e:
        print("Exception is:- ", e)


def inputText(element, text):
    try:
        wait = WebDriverWait(driver=chromeDriver, timeout= utilities.config.maximumTimeout)
        wait.until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR), element).send_keys(text)
    except Exception as e:
        print("Exception is:- ", e)
