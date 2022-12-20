import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from test5_Framework.xyz.BaseClass import BaseClass

from test5_Framework.pageobjects.Login_page import Login_page

from test5_Framework.pageobjects.inbox_page import inbox_page

from test5_Framework.pageobjects.new_mail_page import new_mail_page

from test5_Framework.pageobjects.sent_items_page import sent_items_page


class Test_e2e(BaseClass):
    def test_formSubmission(self):
        logger = self.getLogger()

        testdata_val = self.getTestData("Tc_1")
        logger.debug("Testdata: {}".format(testdata_val))
        loginpage = Login_page(self.driver, testdata_val["email"], testdata_val["password"])
        assert loginpage.enter_email()
        logger.info("successfully entered email")
        assert loginpage.enter_password()
        logger.info("successfully entered password")
        logger.info("successfully Logged in")

        inboxpage = inbox_page(self.driver)
        assert inboxpage.mail_compose()

        new_mail_page_obj =new_mail_page(self.driver, testdata_val["receiver_email"],testdata_val["receiver_email_subject"],testdata_val["receiver_email_message_body"])
        assert new_mail_page_obj.send_new_mail()
        logger.info("successfully sent message")
        assert new_mail_page_obj.check_sent_message_alert()
        logger.info("successfully got acknowledgement")
        inboxpage.check_sent_messages()
        logger.info("Moving to check the sent item")
        sentitemspage =sent_items_page(self.driver)

        output = sentitemspage.get_latest_sent_mail_details()
        logger.info("Successfully got sent mail details")
        logger.debug("output_email: {}".format(output[0]))
        logger.debug("output_subject: {}".format(output[1]))
        logger.debug("output_message_body: {}".format(output[2]))
        output_email= output[0]
        output_subject = output[1]
        output_message_body = output[2]
        #logger.info ("---/n", output_message_body, "---/n",output_subject, "---/n", output_email)
        assert (testdata_val["receiver_email_message_body"] == output_message_body ) and (output_subject == testdata_val["receiver_email_subject"]) and (output_email+"@gmail.com" == testdata_val["receiver_email"])
        logger.info("Successfully Executed Testcase")


