# 2 битовое разреженное число
# print("{0:b}".format(18432))


def countsetbits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


# Program to test function countSetBits
# i = 18432
# print(countSetBits(i))

# This code is contributed by
# Smitha Dinesh Semwal

def nth_sparse(n):
    if n == 1:
        return 3
    count = 1
    num = 3
    while count < n:
        num += 1  #
        if is_sparse(num):
            count += 1
    return num % 35184372089371


def is_sparse(num):
    if countsetbits(num) == 2:
        return True
    else:
        return False


# print(nth_sparse(7))

# while True:
#     data = input('input')
#     count = int(data[0])
#     # result = []
#     # count = int(data[0])
#     # for i in range(0, count):
#     #     # print(i)
#     #     result.append(12)
#     # print(*result, sep='\n')


lines = []
line = input('First line: ')
counter = int(line)
while counter > 0:
    line = int(input('Next line: '))
    lines.append(line)
    counter -= 1
# print(lines)
data = lines
# print(data)
result = []
for i in data:
    result.append(nth_sparse(i))
print(*result, sep='\n')
