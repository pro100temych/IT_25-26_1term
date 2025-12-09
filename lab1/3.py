from copy import deepcopy

numbers = [7, 2, 5]
numbers.append(4)
numbers.insert(1, 10)
numbers.extend([1, 1, 1])
numbers.remove(7)
pop = numbers[-1]
numbers.pop()
numbers.sort()
numbers.reverse()
c2 = numbers.count(2)
i1 = numbers.index(1)
copy1 = numbers.copy()
copy2 = deepcopy(numbers)
numbers.clear()
print(copy1, copy2)