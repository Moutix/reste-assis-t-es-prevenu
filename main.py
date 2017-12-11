""" Little script which display out next incomming metro """

import collections

import requests

URL = "https://api-ratp.pierre-grimaud.fr/v3/schedules/{type}/{line}/{station}/{dest}"

LINE = 8
LINE_NOCTILIENS = [32, 35]
STATION = "maisons+alfort+les+juilliottes"
STATION_NOCTILIEN = "viet"

LINES = [
    ("metros", 8, "maisons+alfort+les+juilliottes", "A+R"),
    ("noctiliens", 32, "viet", "R"),
    ("noctiliens", 35, "viet", "R"),
]


def get_schedules(line, station, ttype="metros", dest="A+R"):
    """ Get the next metro for a given station and line """

    try:
        res = requests.get(URL.format(type=ttype, line=line, station=station, dest=dest)).json()
    except requests.RequestException as err:
        print("Fail to fetch data from %s: %s", URL, err)
        return []

    identifier = "%s%s"% (ttype[0].upper(), line)

    result = collections.defaultdict(list)
    for data in res["result"].get("schedules", []):
        time = data["message"].split(" ")[0]
        try:
            time = int(time)
        except ValueError:
            continue

        result[data["destination"]].append(time)

    return [[identifier, k, v] for k, v in result.items()]

def get_all_schedules(lines=LINES):
    """ Get all the schedules for the given lines """

    for ttype, line, station, dest in lines:
        yield from get_schedules(line, station, ttype, dest)

def main():
    """ Main script """
    print(list(get_all_schedules()))

if __name__ == "__main__":
    main()
