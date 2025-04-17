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

# data = pandas.read_csv("weather_data.csv")

# # data_dict = data.to_dict()
# # # print(data_dict)

# # temp_list = data["temp"].to_list()
# # # average =sum(temp_list)/len(temp_list)

# # # print(average)
# # max_temp = data["temp"].max()
# # print(data[data.temp == max_temp ])
# monday = data[data.day == "Monday"]
# c = monday.temp
# f = (c * 9/5) + 32
# print(f)

data_dict = {
    "student": ["mayank","ravi","ajay"],
    "marks": [43,32,45]
}

data =pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")