import time
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://refugio-animales.herokuapp.com/"
driver.get(url)

usern = "usuario3"

time.sleep(2)
driver.find_element_by_id("registro").click()
time.sleep(2)
driver.find_element_by_name('first_name').send_keys(usern)
driver.find_element_by_name('last_name').send_keys(usern)
driver.find_element_by_name('username').send_keys(usern)
driver.find_element_by_name('email').send_keys(usern+"@gmail.com")
driver.find_element_by_name('password1').send_keys('pass2018')
driver.find_element_by_name('password2').send_keys('pass2018')
time.sleep(1)
driver.find_element_by_id('btnRegistro').click()

time.sleep(2)
driver.find_element_by_name('username').send_keys(usern)
driver.find_element_by_name('password').send_keys('pass2018')
driver.find_element_by_id('btnLogin').click()

# username.send_keys('usuario')
# password.send_keys('pass2018')
# time.sleep(5)
# submit_button.click()
# driver.quit()
