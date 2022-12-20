from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class new_mail_page:

    def __init__(self,driver, receiver_email, receiver_subject, receiver_message_body):
        self.driver = driver
        self.receiver_email = receiver_email
        self.receiver_subject = receiver_subject
        self.receiver_message_body = receiver_message_body


    # receiver_email_ele = (By.XPATH, '//*[@id=":ns"]')
    # receiver_subject_ele = (By.ID, ":jw")
    # receiver_message_body_ele = (By.ID, ":l3")
    # send_btn = (By.ID, ":jm")

    receiver_email_ele = (By.XPATH, '/html/body/div[23]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input')
    receiver_subject_ele = (By.NAME, "subjectbox")
    receiver_message_body_ele = (By.XPATH, '//*[@id=":9n"]')
    send_btn = (By.ID, ":86")


    message_sent_alert = (By.XPATH, '//div[@role="alert"]')
    #message_sent_alert = (By.XPATH, '/span/span[1]]')



    def send_new_mail(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.receiver_email_ele)))
            print("1")
        except:
            return False
        self.driver.find_element(*new_mail_page.receiver_email_ele).send_keys(self.receiver_email)
        print("2")
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.receiver_subject_ele)))
        except:
            return False
        self.driver.find_element(*new_mail_page.receiver_subject_ele).send_keys(self.receiver_subject)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.receiver_message_body_ele)))
        except:
            return False
        self.driver.find_element(*new_mail_page.receiver_message_body_ele).send_keys(self.receiver_message_body)
        try:
            print("4")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.send_btn)))
            print("5")
        except:
            return False
        self.driver.find_element(*new_mail_page.send_btn).click()
        print("=====================dxxxxxxxxxxxxxxxxxxxxx========================")
        return True


    def check_sent_message_alert(self):
        try:
            print("=====================jjbsfjad========================")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.message_sent_alert)))
        except:
            return False
        text = self.driver.find_element(*new_mail_page.message_sent_alert).text
        while("Message sent" in text):
            self.driver.implicitly_wait(10)
            text = self.driver.find_element(*new_mail_page.message_sent_alert).text
            print("---",text)
        print("message sent successfully")
        print("Success-check_sent_message_alert")
        return True