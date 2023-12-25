from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask
from scrap import scrap
from cron import cronCall
from db import db
import schedule

app = Flask(__name__)
scrap()
schedule.every().hours.do(cronCall)

@app.route('/')
def home():
	return db.get("status")

@app.route('/cron')
def cron():
	cronCall()
	return db.get("status")

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug= os.environ["ENV"] == "dev")
