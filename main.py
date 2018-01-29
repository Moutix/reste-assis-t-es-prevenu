""" Little script which display out next incomming metro """
import time
from ht1632 import HT1632C
from wifi import *
from config import *
from ratp_api import *

def main():
	ConnectWifi(SSID, PASSWORD)
	time.sleep(10)
	led = HT1632C(DATAPIN, CLKPIN, CSPIN)
	led.fill(0)
	led.show()
	M8MALJ = LINES[0]
	SchM8MALJ = Schedules(M8MALJ[0], M8MALJ[1], M8MALJ[2], M8MALJ[3])
	while True:
		Sched = []
		while Sched == [] :
			Sched = SchM8MALJ.getSchedules()
		sc = str(Sched)
		print(sc)
		led.text(sc, 0, 0)
		leng = 10*len(sc)
		while leng > 0:
			led.scroll(-1,0)
			led.show()
			leng -= 1
		#time.sleep(20)
		led.fill(0)

if __name__ == "__main__":
	main()
