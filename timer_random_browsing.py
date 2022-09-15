from threading import Timer
from mailtm import Email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chop = webdriver.ChromeOptions()
chop.add_extension("extension_1_2_1_0.crx")
proxy = '199.16.55.252:3561'
# chop.add_argument('--proxy-server=socks5://' + proxy)
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chop)

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()


def hello():
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

if __name__ == "__main__":
    setInterval(15, hello) # every 2 seconds, "do something" will be printed