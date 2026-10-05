area = float(input('Enter area of one wall: '))
interior_cost = float(input('Enter interior cost: '))
exterior_cost = float(input('Enter exterior cost: '))

total_area = area * 8

cost1 = total_area * interior_cost
cost2 = total_area * exterior_cost

print('Interior cost is: ', cost1)
print('Exterior cost is: ', cost2)
print('Total cost is: ', cost1 + cost2)

