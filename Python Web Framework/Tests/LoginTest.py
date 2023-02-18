from utilities import ActionPages, config, Locators
from Pages import LoginPage
import pytest


def logInTest():
    ActionPages.openWebDriver()
    ActionPages.navigateLink(config.URL)
    LoginPage.inputUserName(Locators.userNameField, config.userName)
    LoginPage.inputPassword(Locators.userPasswordField, config.userPassword)
    LoginPage.clickOnLoginButton(Locators.loginButton)


logInTest()
