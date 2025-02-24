from flat import Bill, Flatmate
from reports import PdfReport

#Asking user for input, like amount, timeframe, flatmate
# names and number of days they stay at home
amount = float(input("Please the amount. "))
period = input("Please enter Month and Year. ")
name1 = input("First flatmate name? ")
name1_days = int(input(f"How many days {name1} stayed at home? "))
name2 = input("Second flatmate name? ")
name2_days = int(input(f"How many days {name2} stayed at home? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, name1_days)
flatmate2 = Flatmate(name2, name2_days)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)