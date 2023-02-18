from selenium import webdriver

# /Users/shorya/.jenkins/secrets/initialAdminPassword
# b7d899b121f64f6db8b6dc228920a1b7 - Jenkins Passcode
# This may also be found at: /Users/shorya/.jenkins/secrets/initialAdminPassword

driver = webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
