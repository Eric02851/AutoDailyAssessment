# AutoDailyAssessment  
AutoDailyAssessment automatically takes the daily assessments for robotics class and emails you a copy of the response after class every day.  
 
# Installation
 
 ### Required:
 * lxml
 * bs4
 * requests
 * schedule  
  
```
python3 -m pip install -r requirements.txt
```
 
### Enable less secure app access to recive emails from python 
```
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PCeo67OZq3z468WiSBD-IxJobTyyiUxg2lDfTmMGlCiRvShYKHVzWrYfPV15gYLTrMqPP2NtaserESeGNXtXC26E0zSQ  
```
 
### Fill out config.py with your info
```
 email = ""
 emailPassword = ""
 canvasPassword = ""
 studentName = ""
 studentId = ""
```
# Run
```
python3 main.py
```
