import csv

customers = open("customers.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

for record in customer_file:
    print(record)

    print("ID:", record[1])
    print("EmpFName:", record[2])
    print("EmpLName:", record[3])
    print("Salary:", record[4])
    print("Bonus:", record[5])

for row in reader:
    first_name = row[1]
    last_name = row[2]
    country = row[4]

    display = [first_name, last_name, country]
    writer.writerow(display)
