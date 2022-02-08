import json
from mytime import sleep


def get_cookies(browser):
    sleep(40)
    with open('cookies.txt', 'w') as f:
        f.write(json.dumps(browser.get_cookies()))


def set_cookies(browser):
    browser.delete_all_cookies()
    with open('cookies.txt', 'r') as f:
        cookies_list = json.load(f)
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            browser.add_cookie(cookie)
        browser.refresh()
