import schedule
import time
from datetime import date
from post import post
from urlLocator import spliceUrl

def doAssessment():
    class today:
        month = str(date.today().month)
        day = str(date.today().day)
        year = str(date. today().year)

    url = spliceUrl(today)
    if url != False:
        post(url, today)
    else:
        print("No Assessment Today")

schedule.every().day.at("14:45").do(doAssessment)

while 1:
    schedule.run_pending()
    time.sleep(1)