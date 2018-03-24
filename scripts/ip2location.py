from bs4 import BeautifulSoup
import time

geo_locate_ip= "https://www.ip2location.com/"
def get_location(driver):
	driver.get(geo_locate_ip)
	time.sleep(15)
	page= driver.page_source
	soup = BeautifulSoup(page)

	zipcode=soup.find('label', {'id': 'zipCode'})
	time.sleep(5)
	return zipcode.getText()