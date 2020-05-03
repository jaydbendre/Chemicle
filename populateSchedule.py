import mysql.connector
import random
import datetime

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "chemicalLabdb"
)

cursor = conn.cursor()

for i in range(500):
    year = 2020
    month = 4
    day = random.randint(1,30)
    hour = random.randint(0,23)

    date = str(year)+ "-"+str(month)+"-"+str(day)
    start_time = str(hour) + ":00"
    end_time = str(hour) + ":30"

    data = {
    "date" : str(datetime.datetime.strptime(date , "%Y-%m-%d").date()),
    "start_time" : str(datetime.datetime.strptime(start_time , "%H:%M").time()),
    "end_time" : str(datetime.datetime.strptime(end_time , "%H:%M").time()),
    "description" : "Lorem ipsum",
    "added_by_id" : 10002,
    "lab_id" : 1004,
    "event_type" : random.randint(0,2),
    "title" : "This is a new notification"
    }

    cursor.execute('''INSERT INTO lab_schedule(date,start_time,end_time,description,added_by_id,lab_id,event_type,title) 
    values(
    '{}','{}','{}','{}',{},{},{},'{}'
    )'''.format(
        data["date"],
        data["start_time"],
        data["end_time"],
        data["description"],
        data["added_by_id"],
        data["lab_id"],
        data["event_type"],
        data["title"]
    ))

    conn.commit()