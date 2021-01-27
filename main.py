import requests
import re
from datetime import date 

viewUrl = "https://docs.google.com/forms/d/e/1FAIpQLSc4L1SgNfwyKWw5-vZI6mc-viX515-jDMDgYOybx5Btyzj2ww/viewform"
responseUrl = "https://docs.google.com/forms/d/e/1FAIpQLSc4L1SgNfwyKWw5-vZI6mc-viX515-jDMDgYOybx5Btyzj2ww/formResponse"
s = requests.Session()

getResponse = str(s.get(viewUrl).text)
index = getResponse.find('''[[997277672,"Today's Code",null,0,[[192437282,null,1,null,[[2,100,["''')
indexEnd = getResponse.find('''"]
,"Nope. Wrong answer."]''')

todaysCode = getResponse[index+68:indexEnd]
print(todaysCode)

month = str(date.today().month)
day = str(date.today().day)
year = str(date. today().year)
print(month)
print(day)
print(year)

form_data = {
    "entry.192437282": todaysCode,

    "entry.1374497096": "114966",

    "pageHistory": "",

    "entry.495808885": "Eric Still",

    "entry.1995648639": "10.0",

    "entry.1241598149_year": year,

    "entry.1241598149_month": month,

    "entry.1241598149_day": day,

    "pageHistory": "0,1"
}

postResponse = s.post(responseUrl, data=form_data)
print(postResponse)