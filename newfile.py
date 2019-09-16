#u18/fns/mth/1041
#Paul Felix Okoro
# a program that calculate how many month it takes a user to purchase his dream house.
annualSalary = float(input("enter your annualSalary:"))
portionDownPayment = float(input("enter the portion down percentage:"))
totalCost = float(input("enter the totalCost:"))
monthlySalary =(annualSalary/12)
portionSave = (portionDownPayment/100)
outPut = ("number of month:",(totalCost/portionSave)*monthlySalary)
print(outPut)
#enter your annualSalary:    500000
#enter the portion down percentage:0.500                     enter the totalCost:6000000                                 ('number of month:', 50000000000000.0)                      [Program finished]