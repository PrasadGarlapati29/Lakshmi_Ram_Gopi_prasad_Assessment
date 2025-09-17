# Problem-3 : Odd numbers conditionally

a = 6   # input value
num = 1
count = 0

if a % 2 == 0:   # if a is even
    limit = a - 1
else:
    limit = a

while count < limit:
    print(num, end=" ")
    num = num + 2
    count = count + 1

