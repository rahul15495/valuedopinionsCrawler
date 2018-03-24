from selenium import webdriver
import stem.process
from stem import Signal
from stem.control import Controller
import sys

def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def get_driver():

	#driver_path= "I:\\selenium\\drivers\\"
	driver_path= sys.argv[1]
	driver_name="chromedriver.exe"

	PROXY = "socks5://127.0.0.1:9150"

	webdriver.DesiredCapabilities.CHROME['proxy'] = {
	    "httpProxy":PROXY,
	    "ftpProxy":PROXY,
	    "sslProxy":PROXY,
	    "proxyAutoconfigUrl":None,
	    "noProxy":None,
	    "proxyType":"MANUAL",
	    "class":"org.openqa.selenium.Proxy",
	    "autodetect":False
	}



	driver= webdriver.Chrome(driver_path+driver_name)
	return driver