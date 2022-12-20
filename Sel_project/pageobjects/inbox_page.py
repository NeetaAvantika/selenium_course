from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class inbox_page:
    def __init__(self, driver):
        self.driver = driver

    compose_btn = (By.XPATH, '//div[@class="T-I T-I-KE L3"]')
    #new_mail_compose_box= (By.XPATH, '//*[@id=":c0"]')
    new_mail_compose_box = (By.XPATH, '/html/body/div[23]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input')
    sent_messages_btn = (By.LINK_TEXT, 'Sent')
    sent_page_url ="https://mail.google.com/mail/u/0/#sent"

    def mail_compose(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.compose_btn)))
        except:
            return False
        self.driver.find_element(*inbox_page.compose_btn).click()
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.new_mail_compose_box)))
        except:
            return False
        print("Success-mail_compose")
        return True


    def check_sent_messages(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sent_messages_btn))
        except:
            return False
        self.driver.find_element(*inbox_page.sent_messages_btn).click()
        try:
            WebDriverWait(self.driver, 20).until(EC.url_contains(self.sent_page_url))
        except:
            return False
        print("Success-check_sent_messages")
        return True


