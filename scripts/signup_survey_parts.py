from selenium import webdriver
import time
from bs4 import BeautifulSoup
from collections import defaultdict
import random
import sys


#driver_path= "I:\\selenium\\drivers\\"
driver_path= sys.argv[1]
driver_name="chromedriver.exe"

username= "******"
password="*****"
homepage="https://www.valuedopinions.co.in/"


def open_homepage():
	driver= webdriver.Chrome(driver_path+driver_name)
	driver.get(homepage)

	login_label_id= "loginLabel"
	username_id= "username"
	password_xpath= 'id("password")'
	login_xpath= "//input[@value='Login']"

	time.sleep(10)
	driver.find_element_by_id(login_label_id).click()
	username_element= driver.find_element_by_id(username_id)
	password_xpath_element= driver.find_element_by_xpath(password_xpath)
	login_xpath_button= driver.find_element_by_xpath(login_xpath)

	username_element.send_keys(username)
	password_xpath_element.send_keys(password)
	login_xpath_button.click()
	
	return driver

def inside_profile(driver):
	time.sleep(10)
	driver.find_element_by_xpath('//a[@href= "profile.html"]').click()
	return driver

	return driver
def radio_btn(driver):
	time.sleep(10)
	quest_dict= defaultdict(list)
	page= driver.page_source
	soup = BeautifulSoup(page)
	for tags in soup.find_all('input'):
		quest_dict[tags.attrs['id'].split('_')[1]].append(tags)

	answers = [random.choice(quest_dict[options]) for options in list(quest_dict.keys())]

	get_id= lambda tag: tag.attrs['id']
	answer_id= list(map(get_id,answers))
	for ans in answer_id:
		driver.find_element_by_id(ans).click()
	return driver

def select_tag(driver):
	time.sleep(10)

	page= driver.page_source
	soup= BeautifulSoup(page)
	for tags in soup.find_all('select'):
		tag_id= tags.attrs['id']
		options_tags=[c.attrs['value'] for c in tags.contents]
		options_tags.sort()
		answer= random.choice(options_tags[1:])
		xpath_ans= "//select[@id='{}']".format(tag_id)+"//option[@value='{}']".format(answer)
		driver.find_element_by_xpath(xpath_ans).click()
	return driver

def step_1(driver):
	driver= radio_btn(driver)
	driver= select_tag(driver)
	try:
		driver.find_element_by_class_name('submit').click()
	except:
		sys.exit(0)
	return driver


if __name__ == '__main__':
	driver= open_homepage()
	driver= inside_profile(driver)
	for i in range(100):
		driver=step_1(driver)
		print(i)


