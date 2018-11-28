import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# 指定chromediver的位置，如果在默认路径，这两行可以省略。
executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"

os.environ["webdriver.chrome.driver"] = executable_path

# 定义配置对象
# options = webdriver.ChromeOptions()

# 指定用户的配置地址，并加载至配置对象中。
# options.add_argument("--user-data-dir=" + r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")

# 此处注意，有两个参数，后面那个参数，一定要写成 chrome_options=XX的形式，否则运行报错。
# browser = webdriver.Chrome(executable_path, chrome_options=options)

driver = webdriver.Chrome(executable_path)

driver.get("http://localhost:9999")


# 模拟登陆
time.sleep(2)
driver.find_element_by_xpath('//input[@type="text"]').clear()
driver.find_element_by_xpath('//input[@type="text"]').send_keys('admin')
time.sleep(1)
driver.find_element_by_xpath('//input[@type="password"]').clear()
driver.find_element_by_xpath('//input[@type="password"]').send_keys('123456')
time.sleep(2)
driver.find_element_by_xpath('//button[@type="submit"]').click()  # 点击登陆按钮

driver.quit()





