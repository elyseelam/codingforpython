basicSalary = float(input("What is your basic salary?:  "))
bonus = float(input("What is your bonus?:  "))
promotionRate = float(input("What is your promotion rate in percentage?:  "))
penalty = float(input("What is your penalty?:  "))
noOfPenalty = float(input("What is number of penalty?: "))

print (type(basicSalary))
print (type(bonus))
print (type(promotionRate))
print (type(penalty))
print (type(noOfPenalty))

netSalary = basicSalary + bonus + (basicSalary * promotionRate) - (penalty * noOfPenalty)

print(f"Your net salary is: ${netSalary}")