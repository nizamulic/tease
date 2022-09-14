# open chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# setup proxy
chop = webdriver.ChromeOptions()

chop.add_extension("extension_1_2_1_0.crx")

# create new Chrome driver object with Chrome extension
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chop)

# driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div").click()


# sign up
driver.get("https://teaserfast.ru/registration/")
time.sleep(5)
# username
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/div/input").send_keys("test")

# email
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/div/input").send_keys("test2")
# /html/body/div[1]/div/div/div[2]/form/div[4]/div/input

# password
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/div/input").send_keys("test")
# /html/body/div[1]/div/div/div[2]/form/div[5]/div/input

# password
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[6]/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[6]/div/input").send_keys("test")
# /html/body/div[1]/div/div/div[2]/form/div[6]/div/input

# asking for finishing captcha
captcha = input("done captcha?Y/n")

if(captcha == "Y"):
    # submit button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/a").click()
# /html/body/div[1]/div/div/div[2]/div[2]/a

# verify

