from selenium import webdriver
import time

obj = webdriver.Chrome('./chromeDriver/chromedriver')
obj.get('http://www.cwb.gov.tw/V7/')
time.sleep(2)
obj.find_element_by_link_text('天氣預報').click()
time.sleep(2)
obj.close()

