from cusorder import customer,order

cus = customer.Customer("Jame","Nontaburi")
odr = order.Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} on {odr.date} is {odr.status}')