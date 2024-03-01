people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Use a lambda function as key to sort by age
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)
