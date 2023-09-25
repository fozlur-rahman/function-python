numbers = [10,50,47,8,4,7, 25]

odd_nums = []

for num in numbers :
    if num %2==1 and num%5==0 :
        odd_nums.append(num)


# sort cut this comprehension
# odd_nums = [num for num in numbers if num %2==1 if num %5==0]

print(odd_nums)