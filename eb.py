import csv

customers = open("customers.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

for record in customer_file:
    print(record)

    Identifier = record[1]
    EmpFName = record[2]
    EmpLName = record[3]
    Salary = record[4]
    Bonus = record[5]
    bonus_calc = Salary * Bonus
    display = [EmpFName, EmpLName, Salary, Bonus]

for row in reader:
    first_name = row[1]
    last_name = row[2]
    country = row[4]

    display = [first_name, last_name, country]
    writer.writerow(display)
