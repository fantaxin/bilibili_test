
from selenium.webdriver.common.by import By
from mytime import sleep
from operate import init, search
from readelements import Element


bp = init()
search(bp, 'Warma')
a = bp.get_ele((By.XPATH, '//div[@class="headline"]/a[2]'))
print(a.text)
a.click()
sleep(0.5)
print(a.text)
