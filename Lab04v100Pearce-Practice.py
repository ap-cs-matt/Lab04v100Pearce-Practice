principal = eval(input('Enter principal: '))
rate =  eval(input("Enter rate: ")) / 1200
months = eval(input("Enter years: ")) * 12
monthlyPayment = round(    (   (rate*(1+rate)**months)   /    ((1+rate)**months -1)    )    * principal,2)

print("Principal:\t\t",principal, "\nRate:\t\t\t", rate *1200, "%\nNumber of Years:\t", months/12, "\nMonthly Payment:\t$", monthlyPayment, "\nTotal Payments:\t\t$", round((monthlyPayment*months),2), "\nTotal Interest:\t\t$", (monthlyPayment*months)-principal)
