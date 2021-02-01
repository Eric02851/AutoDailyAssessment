import requests
import bs4
from hidden import schoolSignIn

def findUrl():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    s = requests.session()
    url = 'https://lgsuhsd.instructure.com/login/canvas'
    r = s.get(url,headers=headers,verify=True)

    soup = bs4.BeautifulSoup(r.text, 'lxml')
    csrf_data = soup.find("input", {"name": "authenticity_token"}).get("value")

    values = {
            "authenticity_token": csrf_data,
            "pseudonym_session[unique_id]": schoolSignIn.email,
            "pseudonym_session[password": schoolSignIn.canvasPassword,
            "pseudonym_session[remember_me": '0'
            }
    r = s.post(url,data=values,headers = headers)
    url = "https://lgsuhsd.instructure.com/courses/20278/pages/Daily%20Assessments"
    r = s.get(url,headers=headers,verify=True)
    return r.text

def spliceUrl(date):
    getResponse = findUrl()
    todaysDate = f"{date.month}/{date.day}"
    dateLen = len(todaysDate)
    dateSearch = getResponse.find(todaysDate)
    if dateSearch != -1:
        indexStart = dateSearch + dateLen + 118
        return getResponse[indexStart:indexStart + 35]
    else:
        return False