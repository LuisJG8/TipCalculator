print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
peopleSplitBill = int(input("How many people to split the bill? "))

totalTip = tip / 100
totalBill = totalTip * bill
totalAmount = totalBill + bill
totalAmountFr = totalAmount / peopleSplitBill
# round(totalAmountFr, 3)

print(f"Each person should pay {"%.2f" % totalAmountFr}")

#   "%.(number to round decimal places)f" % (number to round up),
#   example: 3 to round 12.344521 to 12.345
#   assign float when the number could be a decimal like a bill
#   assign int when the numbers are a whole number like the number of people
#   learn more math haha
