import time
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://refugio-animales.herokuapp.com/"
driver.get(url)

time.sleep(1)
driver.find_element_by_id("registro").click()
first_name = driver.find_element_by_name('first_name')
last_name = driver.find_element_by_name('last_name')
username = driver.find_element_by_name('username')
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')
password2 = driver.find_element_by_name('password2')
submit_button = driver.find_element_by_id('btnRegistro')

username.send_keys('usuario')
password.send_keys('pass2018')
time.sleep(5)
submit_button.click()
driver.quit()
