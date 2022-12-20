
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password


    login_email = (By.ID, "identifierId")
    email_next_btn = (By.ID, "identifierNext")
    login_password = (By.NAME, "Passwd")
    paswd_next_btn = (By.ID, "passwordNext")
    next_page_url = "https://mail.google.com/mail/u/0/#inbox"


    def enter_email(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.login_email)))
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))

        self.driver.find_element(*Login_page.login_email).send_keys(self.email)
        try :
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.email_next_btn)))
        except:
            return False
        self.driver.find_element(*Login_page.email_next_btn).click()
        return True

    def enter_password(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.login_password))
        except:
            return False
        self.driver.find_element(*Login_page.login_password).send_keys(self.password)
        self.driver.find_element(*Login_page.paswd_next_btn).click()

        try:
            WebDriverWait(self.driver, 20).until(EC.url_contains(self.next_page_url))
        except:
            return False
        print("Successful Login")
        return True




