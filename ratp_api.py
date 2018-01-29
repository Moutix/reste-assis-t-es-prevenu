import collections
import urequests

URL = "https://api-ratp.pierre-grimaud.fr/v3/schedules/{type}/{line}/{station}/{dest}"

class Schedules():
	def __init__(self, ttype, line, station, dest="A+R"):
		self.url = URL.format(type=ttype, line=line, station=station, dest=dest)
		self.identifier = "%s%s"% (ttype[0].upper(), line)

	def getSchedules(self):
		""" Get the next metro for a given station and line """
		try:
			res = urequests.get(self.url).json()
		except Exception as err:
			print("Failed to fetch data from {}: {}\nCheck your internet connection.".format(self.url, err))
			return []

		result = {}
		for data in res["result"].get("schedules", []):
			time = data["message"].split(" ")[0]
			try:
				time = int(time)
				if time < 3 :
					continue
			except ValueError:
				continue

			result.setdefault(data["destination"], []).append(time)

		return [[self.identifier, k, v] for k, v in result.items()]

#	def get_all_schedules(lines=LINES):
#		""" Get all the schedules for the given lines """
#
#		for ttype, line, station, dest in lines:
#			yield from get_schedules(line, station, ttype, dest)
