import os 
import pickledb


if not os.path.exists("data.db"):
  os.system("touch data.db && echo '{}' > data.db")

db = pickledb.load('data.db', True)

if not db.get("services"):
  db.set("services",[])

if not db.get("status"):
  db.set("status",[])