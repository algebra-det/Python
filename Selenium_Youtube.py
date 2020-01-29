from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/')

def Search(inpu):
    SearchBox = driver.find_element_by_xpath(inpu)
    SearchBox.send_keys('gustavo santaolalla babel')

SearchBox = driver.find_element_by_xpath('//*[@id="search"]')
SearchBox.send_keys('gustavo santaolalla babel')

SearchBox = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
SearchBox.click()

SearchBox = driver.find_element_by_xpath('//*[@id="dismissable"]')
SearchBox.click()