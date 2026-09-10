#take input
cost = float(input('Enter the cost price:'))
discount = float(input('Enter the discount percentage:'))

#calculate discount amount
discount_amount = (cost + discount) / 100

#calculate selling price
selling_price  = cost - discount

#display result
print('Selling price is:' , selling_price)