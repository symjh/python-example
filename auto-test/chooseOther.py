from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import download

def change(driver):
    current_window = driver.current_window_handle
    all_window=driver.window_handles    # 返回当前会话中所有窗口的句柄。
    for window in all_window:           #通过遍历判断要切换的窗口
        if window != current_window:
            driver.switch_to.window(window)     # 将定位焦点切换到指定的窗口，包含所有可切换焦点的选项
            driver.maximize_window()

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
# chrome_driver = "D:\MyData\huangjh54\AppData\Local\Google\Chrome\Application\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver,options=chrome_options)

# current_window = driver.current_window_handle
# all_window=driver.window_handles    # 返回当前会话中所有窗口的句柄。
# print("all_window:: ",all_window)   # 打印当前所有窗口的句柄 name
# for window in all_window:           #通过遍历判断要切换的窗口
#     print("window::  ",window)
#     if window != current_window:
#         driver.switch_to.window(window)     # 将定位焦点切换到指定的窗口，包含所有可切换焦点的选项
# current_window = driver.current_window_handle   # 获取当前窗口handle name

# print(driver.page_source)

def exportAndDownload(driver):
    # print(driver.page_source)
    change(driver)
    menu1 = driver.find_element_by_xpath("//span[text()='考勤数据']")
    #menu1.get_attribute("outerHTML")
    menu1.click()

    menu2 = driver.find_element_by_xpath("//span[text()='考勤报表']")
    menu2.click()
    # sleep(3)

    driver.switch_to.frame(driver.find_element_by_id('appFrame'))
    export = driver.find_element_by_xpath("//a[text()='导出日报表']")
    print(export.get_attribute("outerHTML"))
    export.click()
    print("等待下载")
    sleep(5)

    driver.switch_to.default_content()
    # print(driver.page_source)
    go_download = driver.find_element_by_xpath("//a[text()='去下载']")
    print(go_download.get_attribute("outerHTML"))

    go_download.click()
    print("下载开始")
    driver.switch_to.frame(driver.find_element_by_id('appFrame'))
    loadA = driver.find_element_by_xpath("//a[text()='下载']")
    print(loadA.get_attribute("outerHTML"))
    print(loadA.get_attribute("href"))
    download.getFile(loadA.get_attribute("href"))
    # download.click()

