import network
import time

wlan = None

def ConnectWifi(ssid,passwd,timeout = -1):
    global wlan
    wlan=network.WLAN(network.STA_IF)                        #create a wlan object
    wlan.active(True)                                        #Activate the network interface
    wlan.disconnect()                                        #Disconnect the last connected WiFi
    wlan.connect(ssid,passwd)                                #connect wifi
    tries = 0
    while(wlan.ifconfig()[0]=='0.0.0.0' or (tries<timeout and timeout>0)):
        tries += 1
        time.sleep(1)
    return (tries<timeout and timeout>0)
