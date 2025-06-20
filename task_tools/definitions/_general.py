import datetime

TODAY = datetime.datetime.now()

DATE_STRING = f"{str(TODAY.day).zfill(2)}-{str(TODAY.month).zfill(2)}-{TODAY.year}"

TIME_STRING = f"{str(TODAY.time().hour).zfill(2)}:{str(TODAY.time().minute).zfill(2)}:{str(TODAY.time().second).zfill(2)}"