from os import times
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
import time

browser = driver
browser.get("https://www.instagram.com/?hl=en")

time.sleep(2)

# Logging in;

username = browser.find_element(by=By.NAME, value="username")


time.sleep(2)

username.send_keys("") # Fill Here With Your Username

password = browser.find_element(by=By.NAME, value="password")

time.sleep(2)

password.send_keys("") # Fill Here With Your Password

time.sleep(3)

login = browser.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
login.click()
time.sleep(6)

saveInfo = browser.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div/div/button")
saveInfo.click()
time.sleep(3)

turnOnNotifications = browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]/button[2]")
turnOnNotifications.click()
time.sleep(3)

browser.get("https://www.instagram.com/") # Add accountThatYouWantToAccess/ here
time.sleep(3)

followersClick = browser.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
followersClick.click()
time.sleep(3)

fBody  = browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")

scroll = 0

file =  open("followers.txt", "w", encoding="UTF-8")

while scroll < 1: # Replace 1 with the needed scroll amount
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + (arguments[0].offsetHeight)/2;', fBody)

    time.sleep(1)
    scroll += 1


followers = browser.find_elements(by=By.CSS_SELECTOR, value=".notranslate._0imsa")

for follower in followers:
    file.write(follower.text + "\n")

file.close()

time.sleep(3)

close = browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[3]/div")
close.click()

# Getting followers done

# Now we're getting followings

time.sleep(3)

followingsClick = browser.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div")
followingsClick.click()

time.sleep(3)

fBody  = browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")

scroll = 0

file2 =  open("followings.txt", "w", encoding="UTF-8")

while scroll < 1: # Replace 1 with the needed amount of scrolls

    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + (arguments[0].offsetHeight)/2;', fBody)
    time.sleep(1)
    scroll += 1

followings = browser.find_elements(by=By.CSS_SELECTOR, value=".notranslate._0imsa")

for following in followings:
    file2.write(following.text + "\n")

close2 = browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[3]/div")
close2.click()

file2.close()