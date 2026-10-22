from collections import defaultdict

dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
]

dd = defaultdict(int)

for department, count in dep:
    dd[department] += 1
print(dd)
