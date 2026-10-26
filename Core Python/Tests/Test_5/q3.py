data = [[101, "Seema", 45000],
        [340, "Rajani", 13000],
        [210, "Tannu", 14000],
        [320, "Suresh", 35000]]

data.sort(key = lambda x: x[2])
for emp in data:
    print(emp)