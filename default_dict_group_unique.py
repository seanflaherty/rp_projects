from collections import defaultdict

dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
    ("Marketing", "Adam Doe"),
    ("Marketing", "Adam Doe"),
]

dep_dd = defaultdict(set)

for department, employee in dep:
    dep_dd[department].add(employee)

print(dep_dd)
