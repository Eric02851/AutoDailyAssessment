import schedule
import time
from datetime import date
from post import post
from urlLocator import spliceUrl
from config import config

def scoreInput():
    if config.autoScore == "0.0":
        score = input("Enter a numerical grade from 1-10 up to the tenths decimal place. ")
        return str(float(score))
    else:
        return str(float(config.autoScore))

def doAssessment():
    class today:
        month = str(date.today().month)
        day = str(date.today().day)
        year = str(date. today().year)

    url = spliceUrl(today)
    if url != False:
        score = scoreInput()
        post(url, today, score)
    else:
        print("No Assessment Today")

if config.useSchedule == False:
    doAssessment()
else:
    schedule.every().day.at("14:45").do(doAssessment)
    while True:
        schedule.run_pending()
        time.sleep(1)