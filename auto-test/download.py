from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import get_browser

def getFile(url):
    browser = get_browser.down_chrome()
    # browser = get_browser.down_ie()
    browser.get(url)
    sleep(10)
    print("下载成功")
    print("退出")
    browser.quit()
