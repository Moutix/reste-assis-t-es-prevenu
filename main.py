""" Little script which display out next incomming metro """
import time
import ht1632
import wifi
import config
import ratp_api

def main():
	led = ht1632.HT1632C(config.DATAPIN, config.CLKPIN, config.CSPIN)
	led.fill(0)
	led.text("Boot", 0, 0)
	led.show()
	wifi.ConnectWifi(config.SSID, config.PASSWORD)
	M8MALJ = config.LINES[0]
	SchM8MALJ = ratp_api.Schedules(M8MALJ[0], M8MALJ[1], M8MALJ[2], M8MALJ[3])
	tries = 0
	sc = ""
	while True:
		Sched = []
		tries = 0
		while Sched == [] and tries < 5 :
			tries += 1
			Sched = SchM8MALJ.getSchedules()
		if Sched == [] :
			sc = "Not available"
		else :
			sc = str(Sched).replace('[','').replace(']','').replace('\'','')

		led.fill(0)
		led.text(' '+sc, 0, 0)
		leng = 8*len(sc)
		time.sleep(0.1)
		while leng > 0:
			time.sleep(0.1)
			led.scroll(-1,0)
			led.show()
			leng -= 1

if __name__ == "__main__":
	main()
