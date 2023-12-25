import json
import requests
import time
import datetime
from db import db

def cronCall():
  services = db.get("services")
  statusAll = []
  for service in services:
    status = {"docker": 0, "dns": 0,
              "DNSname": service['dns'], "port": service['port']}
    now = datetime.datetime.now().strftime("%H:%M:%S")
    try:
      if service['dns'] == "":
        r = requests.get(
            "https://iitmandi.co.in", timeout=3)
      elif service['dns'] == "exodia.co.in":
        r = requests.get(
            "https://" + service['dns'], timeout=3)
      else:
        r = requests.get(
            "https://" + service['dns'] + ".iitmandi.co.in", timeout=3)
      status['dns'] = r.status_code
      # print(r.status_code)
    except requests.exceptions.ConnectionError:
      print("service down")
    except:
      print("issue with dns")

    try:
      r = requests.get("http://" + "14.139.34.11:" +
                      str(service['port']), timeout=3)
      status['docker'] = r.status_code
      # print(r.status_code)
    except requests.exceptions.ConnectionError:
      print("service down")
    except:
      print("issue with port")
    # print("\n")
    statusAll.append(status)

  db.set("status",statusAll)

  with open('status.json', 'w') as outfile:
    json.dump({"servies": statusAll}, outfile)

# cronCall()