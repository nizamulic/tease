from mailtm import Email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chop = webdriver.ChromeOptions()
chop.add_extension("extension_1_2_1_0.crx")
proxy = '199.16.55.252:3561'
# chop.add_argument('--proxy-server=socks5://' + proxy)

webBrowser = webdriver.Chrome('chromedriver.exe', chrome_options=chop)

# first tab. Open google.com in the first tab
webBrowser.get('http://google.com')

# second tab
# execute_script->Executes JavaScript snippet.
# Here the snippet is window.open that means, it
# opens in a new browser tab
# url = "https://facebook.com"
# webBrowser.execute_script("window.open('{}');".format(url))

webBrowser.execute_script("window.open('about:blank', 'secondtab');")

# # It is switching to second tab now
webBrowser.switch_to.window("secondtab")

# In the second tab, it opens geeksforgeeks
webBrowser.get('https://www.geeksforgeeks.org/')

webBrowser.execute_script("window.open('about:blank','thirdtab');")

# It is switching to second tab now
webBrowser.switch_to.window("thirdtab")

# In the second tab, it opens geeksforgeeks
webBrowser.get('https://www.facebook.com/')

webBrowser.switch_to.window("secondtab")
webBrowser.close()
input("dfsf")


# 20 seconds open 3 tabs  
#  close tabs afetr