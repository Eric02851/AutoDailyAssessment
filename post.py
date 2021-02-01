import requests
from hidden import schoolSignIn
import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = schoolSignIn.email
receiver_email = schoolSignIn.email
password = schoolSignIn.emailPassword
context = ssl.create_default_context()

s = requests.Session()

def email(postResponse, todaysCode, shortUrl, date):
    if postResponse == "<Response [200]>":
        message = f"""\
Subject: Assessment {date.month}/{date.day} COMPLETED

Assessment url: {shortUrl}
Assessment Content:
    Today's Code: {todaysCode}
    Student ID Number: {schoolSignIn.studentId}
    Your Full First Name: {schoolSignIn.studentName}
    Date: {date.month}/{date.day}/{date.year}
    Numerical Grade: 10.0
"""
    else:
        message = """
Subject: Assessment {date.month}/{date.day} FAILED
    Something went wrong.
"""
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email Sent")

def getCode_Url(shortUrl):
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

    class getData:
        code = todaysCode
        url = responseUrl
    return getData

def post(shortUrl, date):
    getData = getCode_Url(shortUrl)

    form_data = {
        "entry.280336572": getData.code,

        "entry.1529735670": schoolSignIn.studentId,

        "pageHistory": "",

        "entry.2096777452": schoolSignIn.studentName,

        "entry.985620564": "10.0",

        "entry.1014515718_year": date.year,

        "entry.1014515718_month": date.month,

        "entry.1014515718_day": date.day,

        "pageHistory": "0,1"
    }

    postResponse = str(s.post(getData.url, data=form_data))
    email(postResponse, getData.code, shortUrl, date)