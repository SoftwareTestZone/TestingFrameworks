from utilities import ActionPages

def inputUserName(element, name):
    ActionPages.inputText(element, name)

def inputPassword(element, pwd):
    ActionPages.inputText(element, pwd)

def clickOnLoginButton(element):
    ActionPages.isElementVisibleAndClickable(element)