from tor_proxy import *
from ip2location import get_location
from bs4 import BeautifulSoup
from user_details import *
import random

import time

homepage="https://www.valuedopinions.co.in/"
login_page_btn_xhr= "//a[@href='signup.html']"
firstname_id="firstName"
lastname_id= "lastName"
gender_id= "gender"
day_id= "day"
month_id= "month"
year_id= "year"
zip_code_id="260"
state_id="263"
region_id="262"
email_id= "email"
confirmEmail_id= "confirmEmail"
password_id= "password"
confirmPassword_id="confirmPassword"

def open_homepage():
	switchIP()
	driver= get_driver()
	zipcode= get_location(driver)
	print(zipcode)
	driver.get(homepage)
	time.sleep(5)
	driver.find_element_by_xpath(login_page_btn_xhr).click()
	time.sleep(5)
	return driver,zipcode

def select_tag(driver,tag_id,answer=None):
	time.sleep(5)

	page= driver.page_source
	soup= BeautifulSoup(page)
	tags=soup.find('select', {'id': tag_id}).find_all('option')
	if answer==None:
		options_value=[c.attrs['value'] for c in tags]
		options_value.sort()

		if tag_id== year_id:
			_range=(45,-15)
		else:
			_range= (1,-1)
		answer= random.choice(options_value[_range[0]:_range[1]])
	xpath_ans= "//select[@id='{}']".format(tag_id)+"//option[@value='{}']".format(answer)
	driver.find_element_by_xpath(xpath_ans).click()
	return driver

def text_field(driver,tag_id,value):
	time.sleep(5)
	driver.find_element_by_id(tag_id).send_keys(value)

def fill_form(driver,zipcode):
	driver=select_tag(driver,gender_id,"F")
	driver= select_tag(driver,day_id)
	driver= select_tag(driver,month_id)
	driver= select_tag(driver, year_id)

	text_field(driver,firstname_id,firstName)
	text_field(driver,lastname_id,lastName)
	text_field(driver,zip_code_id,zipcode)
	text_field(driver,email_id,email)
	text_field(driver,confirmEmail_id,email)

	time.sleep(5)
	driver= select_tag(driver, state_id)
	time.sleep(5)
	driver= select_tag(driver, region_id)


if __name__ == '__main__':
	driver,zipcode=open_homepage()
	fill_form(driver,zipcode)




