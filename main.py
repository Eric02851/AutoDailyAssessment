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
        #post(url, today)
        print(url)
    else:
        print("No Assessment Today")
    
    print(post("https://forms.gle/7sxHgKyWfBL2nvtJ9", today))

doAssessment()