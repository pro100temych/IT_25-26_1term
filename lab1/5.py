values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(unique_values)
print(len(unique_values))
other = {2, 4, 5}
print(unique_values & other)
print(unique_values | other)
print(unique_values - other)
print(other - unique_values)