import datetime
import json
import re
from math import sqrt, floor

def to_my_format(date):
    return date.isoformat()[5:]

def from_my_format(date):
    return "2021-"+date

def isocalendar_to_my_format(week, weekday):
    try:
        d = datetime.date.fromisocalendar(2021, week+1, weekday+1)
        return d.strftime("%m-%d")
    except:
        return "*****"

def normalize(r,g,b):
    r,g,b = map(lambda x: x-96, (r,g,b))
    # normalize
    length = r*r+g*g+b*b
    r,g,b = map(lambda x: x/sqrt(length)*300, (r,g,b))
    r,g,b = map(lambda x: int(floor(x)), (r,g,b))
    r,g,b = map(lambda x: min(255, x), (r,g,b))
    return (r,g,b)

def load_tasksByDate():
    with open('tasks.json', 'r') as f:
        raw_data = f.read()
    # remove comments
    tasks = json.loads(re.sub(r"//[^\n]*\n", "", raw_data))
    tasks.append({"name": "Ma", "date": to_my_format(datetime.date.today()), "description": "", "color": "#ff0000"})
    tasksByDate = [[{"date": isocalendar_to_my_format(week, weekday), "tasks": []} for weekday in range(7)] for week in range(53)]
    for task in tasks:
        if "color" not in task:
            r,g,b = map(ord, task["name"][:3].lower())
            r,g,b = normalize(r,g,b)
            task["color"] = "rgb({r},{g},{b})".format(r=r, g=g, b=b)
        d = datetime.date.fromisoformat("2021-"+task["date"])
        _, r,c = d.isocalendar()
        c -= 1
        r -= 1
        tasksByDate[r][c]["tasks"].append(task)
    return tasksByDate

def load_model():
    return load_tasksByDate()[37:]

def weekdays():
    return ["H","K","Sz","Cs","P","Szo","V"]
