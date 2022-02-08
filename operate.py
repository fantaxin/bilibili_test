from selenium import webdriver
from base import BasePage
from cookies import set_cookies, get_cookies
from mytime import sleep
from readelements import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get('https://www.bilibili.com')
    get_cookies(browser)


def init():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get('https://www.bilibili.com')
    set_cookies(browser)
    browser.refresh()
    return BasePage(browser)


def search(bp, content):
    element = Element('elements')
    sleep(2)
    bp.send_key((By.XPATH, element['search_input'][1]), content)
    bp.send_key((By.XPATH, element['search_input'][1]), Keys.ENTER)
    # bp.click_key((By.XPATH, element['search_btn'][1]))
    bp.switch_to_new()


def like(bp):
    element = Element('elements')
    bp.scroll_to(150)
    sleep(2)
    a = bp.get_ele_attribute((By.XPATH, element['like'][1]), 'class')
    bp.click_key((By.XPATH, element['like'][1]))
    sleep(1)
    b = bp.get_ele_attribute((By.XPATH, element['like'][1]), 'class')
    return a, b


def intovideo(bp, num):
    element = Element('elements')
    path = element['video'][1] + '[' + str(num) + ']/a'
    bp.click_key((By.XPATH, path))
    bp.switch_to_new()


def collect(bp):
    element = Element('elements')
    bp.scroll_to(150)
    sleep(2)
    a = bp.get_ele_attribute((By.XPATH, element['collect'][1]), 'class')
    bp.click_key((By.XPATH, element['collect'][1]))
    sleep(2)
    bp.click_key((By.XPATH, element['collect_list'][1]))
    bp.click_key((By.XPATH, element['collect_btn'][1]))
    b = bp.get_ele_attribute((By.XPATH, element['collect'][1]), 'class')
    return a, b


def comment(bp, content):
    element = Element('elements')
    a = content
    bp.scroll_to(800)
    sleep(2)
    bp.send_key((By.XPATH, element['comment_text'][1]), content)
    bp.click_key((By.XPATH, element['comment_btn'][1]))
    sleep(1)
    b = bp.get_ele((By.XPATH, element['my_comment'][1])).text
    return a, b


def zhuifan(bp, num):
    element = Element('elements')
    path = element['fan'][1] + '[' + str(num) + ']/a'
    bp.click_key((By.XPATH, element['fanjv'][1]))
    bp.switch_to_new()
    bp.click_key((By.XPATH, path))
    bp.switch_to_new()
    a = bp.get_ele((By.XPATH, element['zhuifan'][1] + '/span')).text
    bp.click_key((By.XPATH, element['zhuifan'][1]))
    sleep(2)
    b = bp.get_ele((By.XPATH, element['zhuifan'][1] + '/span')).text
    return a, b


def guanzhu(bp):
    element = Element('elements')
    a = bp.get_ele((By.XPATH, element['guanzhu'][1])).text
    bp.click_key((By.XPATH, element['guanzhu'][1]))
    sleep(0.5)
    b = bp.get_ele((By.XPATH, element['guanzhu'][1])).text
    return a, b
