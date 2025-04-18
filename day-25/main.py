import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrels = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels,cinnamon_squirrels,black_squirrels]
}

data = pandas.DataFrame(squirrels)
data.to_csv("new_squirrels.csv")



















# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     next(data)
# #     temperature =[]
# #     for row in data:
# #         temp = int(row[1])
# #         temperature.append(temp)
# #     print(temperature)
# import pandas

# # data = pandas.read_csv("weather_data.csv")

# # # data_dict = data.to_dict()
# # # # print(data_dict)

# # # temp_list = data["temp"].to_list()
# # # # average =sum(temp_list)/len(temp_list)

# # # # print(average)
# # # max_temp = data["temp"].max()
# # # print(data[data.temp == max_temp ])
# # monday = data[data.day == "Monday"]
# # c = monday.temp
# # f = (c * 9/5) + 32
# # print(f)

# # data_dict = {
# #     "student": ["mayank","ravi","ajay"],
# #     "marks": [43,32,45]
# # }

# # data =pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")