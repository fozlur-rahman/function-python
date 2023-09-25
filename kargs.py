# def sum_add (num,num1, *some):
#       sum = f'{num} {num1}'
#       print(sum)
#       for i in some:
#             print(i)

# sum_add(10,40,85,7,4,7,5)

def sum (n,n1):
    add = n+n1
    subs = n-n1
    mult = n*n1

    return add, subs,mult

add = sum(10,20)
print (add)