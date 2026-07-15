Hr_work = int(input("Enter the number of hours worked: "))
Hr_rate = float(input("Enter the hourly rate: "))

if Hr_work <= 40:
    gross_pay = Hr_work * Hr_rate
    print("The Gross pay is $", format(gross_pay, ".2f"))
elif Hr_work > 40:
    overtime_hours = Hr_work - 40
    overtime_pay = overtime_hours * (Hr_rate * 1.5)
    gross_pay = (40 * Hr_rate) + overtime_pay
    print("The Gross pay is $", format(gross_pay, ".2f"))
    