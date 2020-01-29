from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://github.com/login')
username = driver.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys('algebra-det')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Githublogmein987')

login = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
login.click()

goto = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/ul/li[1]/div/a')
next = goto.click()

driver.execute_script("window.scrollTo(0, 700)")
