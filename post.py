import requests

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
    index = getResponse.find('''[[746616177,"Today's Code",null,0,[[280336572,null,1,null,[[2,100,["''')
    indexEnd = getResponse.find('''"]
,"Nope. Wrong answer."]''')

    todaysCode = getResponse[index+68:indexEnd]
    print(todaysCode)
    print(date.month)
    print(date.day)
    print(date.year)

    form_data = {
        "entry.280336572": todaysCode,

        "entry.1529735670": "114966",

        "pageHistory": "",

        "entry.2096777452": "Eric Still",

        "entry.985620564": "10.0",

        "entry.1014515718_year": date.year,

        "entry.1014515718_month": date.month,

        "entry.1014515718_day": date.day,

        "pageHistory": "0,1"
    }

    postResponse = s.post(responseUrl, data=form_data)
    print(postResponse)