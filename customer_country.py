import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

for record in customer_file:

    print(record)

    print("first name:", record[1])
    print("last name:", record[2])
    print("Country:", record[4])

    input()

customer_file.close()
