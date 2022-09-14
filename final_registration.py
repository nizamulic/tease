from mailtm import Email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chop = webdriver.ChromeOptions()
chop.add_extension("extension_1_2_1_0.crx")

driver = webdriver.Chrome('chromedriver.exe', chrome_options=chop)

def listener(message):
    print("\nSubject: " + message['subject'])
    with open('readme.txt', 'w', encoding="utf-8") as f:
        f.write(message['text'] if message['text'] else message['html'])
    # extract a specific line from message
    with open('readme.txt', 'r', encoding="utf-8") as f:
        for line in f:
            if line.startswith('https://teaserfast.ru/registration/?verification='):
                print(line)
                driver.get(str(line))
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener)
print("\nWaiting for new emails...")

username = str(test.address).split("@")[0]
email = str(test.address)
password = username + "123"
with open('addresses.txt', 'w', encoding="utf-8") as f:
      f.write(email)
# sign up
driver.get("https://teaserfast.ru/registration/")
time.sleep(5)
# username
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/div/input").send_keys(username)

# email
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/div/input").send_keys(email)
# /html/body/div[1]/div/div/div[2]/form/div[4]/div/input

# password
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/div/input").send_keys(password)
# /html/body/div[1]/div/div/div[2]/form/div[5]/div/input

# password
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[6]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[6]/div/input").send_keys(password)
# /html/body/div[1]/div/div/div[2]/form/div[6]/div/input

# asking for finishing captcha
captcha = input("done captcha?Y/n")

if(captcha == "Y"):
    # submit button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/a").click()





# tasks:
# get email id and extract before @