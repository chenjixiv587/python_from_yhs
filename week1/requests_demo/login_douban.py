from selenium import webdriver

from selenium.webdriver.common.by import By

import time


browser = webdriver.Chrome()

browser.get('https://www.douban.com/')
browser.switch_to.frame(browser.find_element(
    By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe'))
browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
browser.find_element(
    By.XPATH, '//*[@id="username"]').send_keys('992510191@qq.com')
browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('iloveu')
browser.find_element(
    By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(5)
browser.close()
