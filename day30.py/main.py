try:
    file = open("text.txt")
except FileNotFoundError as error:
    print(error)
    file = open("text.txt","w")
else:
    content = file.read()
finally:
    file.close()
    print("file is closed")
