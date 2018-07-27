# WebDriver 学习
from selenium import webdriver
from time import sleep

# 设置启动选项
start_options=webdriver.ChromeOptions()
# 启动的时候窗口最大化
start_options.add_argument('--start-maximized')

# 启动谷歌浏览器
driver = webdriver.Chrome(chrome_options=start_options)

# "睡"几秒
sleep(1)

# 打开百度
driver.get('https://www.baidu.com/')

# 输入框中输入关键字
driver.find_element_by_id('kw').send_keys('什么')

sleep(1)

driver.find_element_by_id('kw').send_keys('是月食')

# 点击搜索按钮 通过 xPath
driver.find_element_by_xpath('//*[@id="su"]').click()

sleep(3)

# 退出浏览器
driver.quit()

"""
定位的方法【定位单个】
find_element_by_id()        # 通过id定位
find_element_by_name()      # 通过name定位
find_element_by_class_name()# 通过类名定位
find_element_by_tag_name()  # 通过标签名定位
find_element_by_link_text() # 通过超链接文字定位
find_element_by_partial_link_text() # 通过超链接文字模糊定位

下面方法返回的是符合条件的列表【定位多个】
find_elements_by_id()        # 通过id定位
find_elements_by_name()      # 通过name定位
find_elements_by_class_name()# 通过类名定位
find_elements_by_tag_name()  # 通过标签名定位
find_elements_by_link_text() # 通过超链接文字定位
find_elements_by_partial_link_text() # 通过超链接文字模糊定位

XPath定位
find_element_by_xpath()      # 通过路径来定位
    有许多插件能获取到元素的XPath
    我在 FireFox火狐上找到一款插件 【xPath Finder】

CSS 定位
find_element_by_css_selector()

"""