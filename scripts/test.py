from tor_proxy import *
import time

for i in range(2):
	switchIP()
	driver= get_driver()
	driver.get("http://www.icanhazip.com")
	time.sleep(10)







