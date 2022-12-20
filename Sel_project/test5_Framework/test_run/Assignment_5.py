from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time
email = "demouserneeta@gmail.com"
password ="Demo@123"


def assignment_5():
    service_obj = Service("/test5/chromedriver.exe")
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.maximize_window()
    driver.get("https://www.gmail.com")
    input_email ="neeta.chougule05@gmail.com"
    input_subject = "demo"
    input_message_body = "demo text"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"identifierId")))
    driver.find_element(By.ID,"identifierId").send_keys(email)
    driver.find_element(By.ID,"identifierNext").click()
    driver.implicitly_wait(20)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "Passwd")))
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "Passwd").send_keys("Demo@123")
    driver.find_element(By.ID, "passwordNext").click()
    print("success")
    WebDriverWait(driver, 20).until(EC.url_contains("https://mail.google.com/mail/u/0/#inbox"))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="T-I T-I-KE L3"]')))
    driver.find_element(By.XPATH, '//div[@class="T-I T-I-KE L3"]').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id=":c0"]')))
    driver.find_element(By.XPATH,'//*[@id=":c0"]').send_keys(input_email)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,":83")))
    driver.find_element(By.ID,":83").send_keys(input_subject)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,":9a")))
    driver.find_element(By.ID,":9a").send_keys(input_message_body)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,":7t")))
    driver.find_element(By.ID,":7t").click()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="alert"]')))
    text = driver.find_element(By.XPATH, '//div[@role="alert"]').text
    while("Message sent" in text):
        driver.implicitly_wait(10)
        text = driver.find_element(By.XPATH, '//div[@role="alert"]').text
        print("---",text)
    print("message sent successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'Sent')))
    driver.find_element(By.LINK_TEXT,'Sent').click()
    WebDriverWait(driver, 20).until(EC.url_contains("https://mail.google.com/mail/u/0/#sent"))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr[@class="zA yO"][1]')))
    last_sent = driver.find_element(By.XPATH, '//tr[@class="zA yO"][1]')
    last_sent.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr[@class="zA yO"][1]//span[1]')))
    output_message_body = driver.find_element(By.XPATH, '//table[@role="presentation"]//div[@class=""]').text
    output_subject = driver.find_element(By.XPATH, '//table//h2').text
    output_email = driver.find_element(By.CLASS_NAME, 'g2').text

    print ("---/n", output_message_body, "---/n",output_subject, "---/n", output_email)
    if (input_message_body == output_message_body ) and (output_subject == input_subject) and (output_email+"@gmail.com" == input_email):
        print("verified sent mail successfully")






assignment_5()