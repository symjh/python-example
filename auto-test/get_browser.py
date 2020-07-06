from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.ie.options import Options
import os

path = os.getcwd()
download_path = os.getcwd() + "\Downloads"
ie_driver_path = path+"\IEDriverServer.exe"
chrome_driver_path = path+"\chromedriver.exe"
phantomjs_path = path+"\phantomjs"
chrome_path = path+"\Chrome\App\Chrome.exe"

# 无头启动
def headless_ie():
    ieOptions = Options()
    ieOptions.add_argument("--headless")
    browser = webdriver.Ie(executable_path=ie_driver_path, options=ieOptions)
    return browser

# ie正常启动
def normal_ie():
    return webdriver.Ie(executable_path=ie_driver_path)

def down_ie():
    options = Options()
    prefs = {"download.default_directory": download_path,"download.prompt_for_download": False,}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    browser = webdriver.Ie(executable_path=ie_driver_path, options=options)
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
    command_result = browser.execute("send_command", params)
    return browser


# 下载启动
def down_chrome():
    options = Options()
    options.binary_location = chrome_path
    prefs = {"download.default_directory": download_path,"download.prompt_for_download": False,}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
    command_result = browser.execute("send_command", params)
    return browser

# 正常启动
def normal_chrome():
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    browser = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
    return browser

# 无头启动
def headless_chrome():
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    return browser

# 测试模式 使用指定浏览器启动
def test_chrome():
    #指定浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
    browser = webdriver.Chrome(chrome_driver_path,options=chrome_options)
    return browser