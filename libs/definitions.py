import datetime
import json

import pytz
from PIL import ImageFont

current = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))


def getTimeNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%H:%M:%S")


def getFullDateNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%d %m %Y")


def getDateNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%d")


def getMonthNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%m")


def getYearNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%Y")


def getDayOfWeekNow(daysdelta=0, current=current):
    current += datetime.timedelta(daysdelta)
    return current.strftime("%A")


def getCode(content):
    if content.startswith("```python") and content.endswith("```"):
        return content[9:-3]


def addAsync(code):
    return f"async def __async__():\n{code}"


def getMonth(index):
    months = {
        "1": "January",
        "2": "Feburary",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    print(type(months.keys()))
    if str(index) in months.keys():
        return months[str(index)]
    else:
        return False


def visualLengthOfString(path, text, size):
    font = ImageFont.truetype(path, size)
    size = font.getsize(text)
    return size


def jsonload(path):
    with open(path, "r") as f:
        return json.load(f)


def jsondump(path, data, indent=2):
    with open(path, "w") as f:
        json.dump(data, f, indent)
