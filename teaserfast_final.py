# registration
from mailtm import Email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from threading import Timer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('web-tests-60e15-firebase-adminsdk-hdgfk-58b66a5e39.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://web-tests-60e15-default-rtdb.firebaseio.com"
})




def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()


def random_browsing():
    print("do something")
    # driver.execute_script("window.open('http://google.com', 'firsttab');")
    try:
        driver.switch_to.window(driver.window_handles[0])
        print("here 0")
        driver.get('http://google.com')
        print("here 1")
        time.sleep(3)

        driver.execute_script("window.open('https://www.geeksforgeeks.org/');")
        print("here 2")
        time.sleep(3)

        # # It is switching to second tab now
        driver.switch_to.window(driver.window_handles[1])
        print("here 3")

        # In the second tab, it opens geeksforgeeks
        # driver.get('https://www.geeksforgeeks.org/')

        driver.execute_script("window.open('https://www.facebook.com/');")
        print("here 4")
        
        # It is switching to second tab now
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(3)
        # In the second tab, it opens geeksforgeeks
        # driver.get('https://www.facebook.com/')

        # driver.switch_to.window("secondtab")
        # driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        # driver.switch_to.window("firsttab")
        # driver.close()
        # driver.switch_to.window("thirdtab")
    except:
        print("error")

    return False # return True if you want to stop

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
                # random browsing
                setInterval(30, random_browsing)
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
with open('addresses.txt', 'a', encoding="utf-8") as f:
      f.write("\n"+email)

# driver setup
chop = webdriver.ChromeOptions()
chop.add_extension("extension_1_2_1_0.crx")
proxy = '199.16.55.252:3551'   
chop.add_argument('--proxy-server=socks5://' + proxy)
chop.add_argument("--user-data-dir=C:/Users/Administrator/Documents/teaserfast/profiles"+ username)

driver = webdriver.Chrome('chromedriver.exe', chrome_options=chop)

# account details on firebase
ref = db.reference("/accounts")
ref.push().set(
	{
		"email": email,
        "proxy": proxy
	}
)
print(ref.get())

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



#  pyautogui enter