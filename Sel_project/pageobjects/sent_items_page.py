
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class sent_items_page:

    def __init__(self, driver):
        self.driver = driver


    latest_sent_mail_btn = (By.XPATH, '//tr[@class="zA yO"][1]')
    latest_mail_detail_ele = (By.XPATH, '//tr[@class="zA yO"][1]//span[1]')
    sent_mail_msg_body = (By.XPATH, '//table[@role="presentation"]//div[@class=""]')
    sent_mail_subject = (By.XPATH, '//table//h2')
    sent_mail_rcvr_email = (By.CLASS_NAME, 'g2')


    def get_latest_sent_mail_details(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.latest_sent_mail_btn))
        except:
            return False
        last_sent = self.driver.find_element(*sent_items_page.latest_sent_mail_btn)
        last_sent.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.latest_mail_detail_ele)))
        except:
            return False
        output_message_body = self.driver.find_element(*sent_items_page.sent_mail_msg_body).text
        output_subject = self.driver.find_element(*sent_items_page.sent_mail_subject).text
        output_email = self.driver.find_element(*sent_items_page.sent_mail_rcvr_email).text

        output = [output_email,output_subject,output_message_body]
        print("===========", output)
        return output

