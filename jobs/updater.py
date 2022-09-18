from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api, spewApiContent

def start():
    scheduler = BackgroundScheduler()
    #scheduler.add_job(spewApiContent, 'interval', minutes=1)
    scheduler.add_job(schedule_api, 'interval', minutes=5)
    scheduler.start()