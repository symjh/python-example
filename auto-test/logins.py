# coding = utf-8
#模拟浏览器自动登录yahoo邮箱
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chooseOther
import os
import get_browser

def login():
    # 修改模式
    # 不显示浏览器
    # browser = get_browser.headless_chrome()
    # 显示浏览器
    browser = get_browser.normal_chrome()
    # browser = get_browser.headless_ie()

    #设置访问链接
    browser.get("")

    username = ""
    password = ""

    # 页面找寻元素尝试最大等待时间10秒
    browser.implicitly_wait(10)

    # 切换至账号登录
    tabList = browser.find_elements_by_css_selector(".login_tab_item__2zEfz")
    tab = tabList[1]
    tab.click()
    # 输入用户名
    input_name = browser.find_element_by_xpath('//input[@type="text"]')
    input_name.send_keys(username)
    # 输入密码
    input_psw = browser.find_element_by_xpath('//input[@type="password"]')
    input_psw.send_keys(password)

    # 点击登录
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    #点击智能考勤
    dashboardList = browser.find_elements_by_css_selector('.dashboard_col_content__3e813')
    dashboard = dashboardList[0]
    dashboard.click()

    chooseOther.exportAndDownload(browser)

    browser.quit()

if __name__ == '__main__':
    login()