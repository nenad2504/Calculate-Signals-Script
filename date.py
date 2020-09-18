import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

dateFormat = '%Y-%m-%d' # 2020-12-01
# d1 = datetime.strptime('2020-01-01', dateFormat)
# d2 = datetime.strptime('2020-01-06', dateFormat)


def getDates(lastRun, currentDay):
    lastRun = datetime.strptime(lastRun, dateFormat)
    currentDay = datetime.strptime(currentDay, dateFormat)

    dates = []

    while lastRun < currentDay:
        dates.append(lastRun.strftime(dateFormat))
        lastRun += timedelta(days=1)

        if lastRun >= currentDay:
            break

    return dates

LAST_RUN_FILE = os.getenv('LAST_RUN_FILE')

# store in file
def storeLastRunInFile(date):
    # example format '2020-01-01'
    with open(LAST_RUN_FILE, 'w') as f:
        json.dump({'date': date}, f)

# reads last run date from the file
def getLastRunInFile():
    # expected format {"date": "2020-01-30"}
    with open(LAST_RUN_FILE, 'r') as f:
        data = json.load(f)
        return data['date']


# storeLastRunInFile('2020-01-03')

# print(getLastRunInFile())