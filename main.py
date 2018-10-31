import time
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://refugio-animales.herokuapp.com/"
driver.get(url)

time.sleep(3)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
submit_button = driver.find_element_by_id('btnLogin')

username.send_keys('usuario')
password.send_keys('pass2018')
time.sleep(2)
submit_button.click()
driver.quit()
