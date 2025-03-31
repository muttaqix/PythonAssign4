import csv

fileSource = "ApplicationLog.csv"
list = []

with open(fileSource, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 3 and row[2].strip() == "Universal Print":
            date_str = row[1].strip() 
            try:
                dateAndTime = date_str.rsplit(" ", 1)[0]  
                fullDate, fullTime = dateAndTime.split()  
                year, month, day = fullDate.split("-")
                hour, minute, second = fullTime.split(":")

                time = f"{int(hour):>6}:{int(second):>6}"
                date = f"{int(day):>6}:{int(month):>6}:{int(year):>6}"
                list.append(f"{time}\t{date}")
            except Exception:
                continue

for entry in list:
    print(entry)


