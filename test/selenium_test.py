import time

from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()

# 打开web页面
driver.get('https://www.baidu.com/')

# 暂停
time.sleep(3)

# 关闭驱动
driver.close()
