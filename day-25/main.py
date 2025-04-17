# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperature =[]
#     for row in data:
#         temp = int(row[1])
#         temperature.append(temp)
#     print(temperature)
import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# # average =sum(temp_list)/len(temp_list)

# # print(average)
max_temp = data["temp"].max()
print(data[data.temp == max_temp ])
