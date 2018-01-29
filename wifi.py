import network
import time

Wlan = None

def ConnectWifi(ssid,passwd):
	global wlan
	Wlan=network.WLAN(network.STA_IF)						#create a wlan object
	Wlan.active(True)										#Activate the network interface
	Wlan.disconnect()										#Disconnect the last connected WiFi
	Wlan.connect(ssid,passwd)								#connect wifi
	while(Wlan.ifconfig()[0]=='0.0.0.0'):
		time.sleep(1)
	return True
