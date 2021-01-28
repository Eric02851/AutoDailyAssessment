import requests
import re

def post(shortUrl, date):
    s = requests.Session()
    viewUrl = s.get(shortUrl).url
    splitUrl = viewUrl.split('/')

    responseUrl = ""
    for i in range(7):
        responseUrl += (splitUrl[i])
        responseUrl += '/'
    responseUrl += "formResponse"

    getResponse = str(s.get(viewUrl).text)
    index = getResponse.find('''[[997277672,"Today's Code",null,0,[[192437282,null,1,null,[[2,100,["''')
    indexEnd = getResponse.find('''"]
,"Nope. Wrong answer."]''')

    todaysCode = getResponse[index+68:indexEnd]
    print(todaysCode)
    print(date.month)
    print(date.day)
    print(date.year)

    form_data = {
        "entry.192437282": todaysCode,

        "entry.1374497096": "114966",

        "pageHistory": "",

        "entry.495808885": "Eric Still",

        "entry.1995648639": "10.0",

        "entry.1241598149_year": date.year,

        "entry.1241598149_month": date.month,

        "entry.1241598149_day": date.day,

        "pageHistory": "0,1"
    }

    postResponse = s.post(responseUrl, data=form_data)
    print(postResponse)