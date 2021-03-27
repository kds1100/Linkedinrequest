from selenium import webdriver
import login
from time import sleep
import time
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path = r'C:\Users\geckodriver.exe')
driver.get('https://www.linkedin.com/login')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="username"]').send_keys(login.email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(login.passs)
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(3)
search='.search-global-typeahead__input'
search_element=driver.find_element_by_css_selector(search)
search_element.send_keys('looking for digital marketing')
search_element.send_keys(Keys.RETURN)
sleep(5)
driver.find_element_by_xpath("//button[text()='People']").click()
sleep(5)
driver.find_element_by_xpath("//span[text()='Karan Mahajan']").click()
# elementone=driver .find_element_by_xpath("//button[class()='artdeco-button artdeco-button--2']")
# elementone.click()
sleep(5)
driver.find_element_by_xpath("//span[text()='Connect']").click()
sleep(3)
driver.find_element_by_xpath("//span[text()='Add a note']").click()
sleep(3)
driver.find_element_by_xpath("//*[@id='custom-message']").send_keys('Hello, are you looking for a job change in Digital Marketing?')
sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span").click()





































































































































#ember19 > input
# driver.get('https://www.linkedin.com/search/results/people/?keywords=looking%20for%20digital%20marketing&origin=SWITCH_SEARCH_VERTICAL')
# time.sleep(3)
# driver.get('https://www.linkedin.com/in/karan-mahajan-a743b1195/')
# time.sleep(5)
# driver.find_element_by_id('ember2404').click()
# # driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]/span').click()
# driver.find_element_by_xpath('//*[@id="custom-message"]').send_keys('Hi, are you looking for a Digital Marketing Opportunity?!')

#
# frame=driver.find_element_by_class_name('pv2 artdeco-card ph0 mb2')
# driver.switch_to_frame(frame)
# connect_button=driver.find_element_by_id("ember148")
# connect_button.click()

# driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div/div[1]/main/div/div/div[2]/ul/li[1]/div/div/div[3]/button/span').click()


# category='/html/body/div[8]/div[3]/div/div[1]/div/div[1]/main/div/div/div[1]/div/a'
# search_category=driver.find_element_by_xpath(category)
# search_category.click()


