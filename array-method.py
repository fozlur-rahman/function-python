numbers = [10,50,47,8,4,7]

numbers.append(12)
numbers.insert(1, 50)   #for inset value in index wise of array 
numbers.remove(10)

# use condition for valid
if 10 in numbers:
    numbers.remove(10)

numbers.pop()
numbers.sort()
numbers.reverse()
if 10 in numbers:
    index_it =  numbers.index(10)

# print(index_it)