from collections import defaultdict

dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
]

dep_dd = defaultdict(list)

for department, employee in dep:
    dep_dd[department].append(employee)

print(dep_dd)
