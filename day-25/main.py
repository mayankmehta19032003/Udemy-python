import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperature =[]
    for row in data:
        temp = int(row[1])
        temperature.append(temp)
    print(temperature)