from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg
import time

song = input("song: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/?safe=active&ssui=on")
time.sleep(1)
pg.typewrite(song + " lyrics")
pg.press("enter")

try:
    print(driver.find_element(By.XPATH, value='//*[@id="kp-wp-tab-default_tab:kc:/music/recording_cluster:lyrics"]/div[1]/div/div').text)
    driver.close()
except:
    print(driver.find_element(By.XPATH, value='//*[@id="rso"]/div[1]/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]').text)
    driver.close()
