import csv
import random
from datetime import datetime, timedelta

products = ["Laptop","Phone","Shoes","Watch","Tablet","Headphones","Camera"]
categories = ["Electronics","Fashion","Accessories"]
regions = ["North","South","East","West"]

start_date = datetime(2023,1,1)

rows = []

for i in range(1,3001):

    product = random.choice(products)
    category = random.choice(categories)
    price = random.randint(1000,60000)
    quantity = random.randint(1,5)
    total_sales = price * quantity
    region = random.choice(regions)

    order_date = start_date + timedelta(days=random.randint(0,365))

    rows.append([
        i,product,category,price,quantity,total_sales,region,order_date.date()
    ])

with open("sales_data.csv","w",newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Order_ID","Product","Category","Price",
        "Quantity","Total_Sales","Region","Order_Date"
    ])

    writer.writerows(rows)

print("3000 Sales Records Generated Successfully")