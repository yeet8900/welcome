from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import urllib.request
from selenium.webdriver.support.ui import Select
import time

b=webdriver.Firefox()
for i in range(1,1000):
    k=str(i)
    u="https://xkcd.com/"+k
    b.get(u)
    z=b.find_element(By.XPATH,"/html/body/div[2]/div[2]/img")
    src = z.get_attribute('src')
    o="lol"+k +".png"
    urllib.request.urlretrieve(src, o)