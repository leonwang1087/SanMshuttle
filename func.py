import datetime
import pytz
from time import sleep
from requests import Session
import json

def getTime():
    url = "https://peninsulashuttles.com/Stop/3245356/Arrivals"
    header = {"Content-Type": "Application/json"}
    s = Session()
    response = s.get(url=url, headers=header)
    data = json.loads(response.text)
    nextTime = data[0]["Arrivals"][0]["ArriveTime"]
    return nextTime
    
def writeResult(nextTime):
    with open("./result.txt", "w") as f:
        f.write(nextTime)

def main():
    while True:
        now = datetime.datetime.now(tz=pytz.timezone("America/Los_Angeles"))
        if now.hour >= 16 and now.hour <= 19:
            if now.hour == 16 and now.minute > 50:
                nextTime = getTime()
                writeResult(nextTime)
                sleep(10 * 60)
            elif now.hour > 16:
                nextTime = getTime()
                writeResult(nextTime)
                sleep(20 * 60)
            else:
                sleep(30 * 60)
        else:
            sleep(3600)
            

if __name__ == "__main__":
    main()