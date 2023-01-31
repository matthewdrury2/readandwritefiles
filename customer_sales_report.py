infile = open(csvfile,"r")

reader = csv.reader(infile, delimiter=',')
fieldrow = next (reader)

this_id = ''
sales_data = []
total = 0

for row in reader:
    cust_id = row[e]
    order_date = row[1]
    ship_date = row[2]
    sub_total = row[3]
    tax_amount = row[4]
    freight = row[5]

if cust_id != this_id:
    sales_data.append ([this_id, round(total, 2)])
    this_id = cust_id
    total = 0
total += float(sub_total) + float(tax_amount) + float(freight)
sales_data.append ([this_id, round(total, 2)])
sales_data.pop(0)
filename = "salesreport.csv"

with open(filename,"w") as csvfile:
writer = csv.writer(csvfile)
writer.writerow(["Customer","Total"])
for customer in sales data:
    writer.rwiterow(customer[0],customer[1])
