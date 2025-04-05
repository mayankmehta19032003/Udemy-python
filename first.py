bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill? ")

totalAmt = float(bill) + float(tip)
eachPay = totalAmt / float(people)
print("Each person should pay: $ " , float(eachPay))