# 2 битовое разреженное число print("{0:b}".format(18432)) N-битовое разреженное число — это число, в бинарной записи
# которого присутствует ровно N единиц - все остальные нули. Например число 137 — 3-битовое разреженное, потому что в
# двоичной системе записи выглядит как 10001001.
#
# Рассмотрим все 2-битовые разреженные числа, упорядоченные по возрастанию. Необходимо найти k-тое по порядку число в
# этой последовательности.
#
# Ответ необходимо дать по модулю числа 35184372089371 (остаток от деления на это число).
#
# Пояснение к примерам:
#
# Последовательность начинается следующим образом: 3 (11), 5 (101), 6 (110), 9 (1001), 10 (1010), 12 (1100), 17 (10001).
# Таким образом первое число - 3, второе - 5, седьмое - 17.

def nextsparse(x):
    # Find binary representation of
    # x and store it in bin[].
    # bin[0] contains least significant
    # bit (LSB), next bit is in bin[1],
    # and so on.
    bin_rep = []
    while x != 0:
        bin_rep.append(x & 1)
        x >>= 1

    # There my be extra bit in result,
    # so add one extra bit
    bin_rep.append(0)
    position = len(bin_rep)  # Size of binary representation

    # The position till which all
    # bits are finalized
    changes = 0

    # Start from second bit (next to LSB)
    for m in range(0, position - 2):

        # If current bit and its previous
        # bit are 1, but next bit is not 1.
        if bin_rep[m] == 1 and bin_rep[m + 1] != 1:
            # Make the next bit 1
            bin_rep[m + 1] = 1
            bin_rep[m] = 0
            changes += 1
            break

            # # Make all bits before current
            # # bit as 0 to make sure that
            # # we get the smallest next number
            # for j in range(i, last_final - 1, -1):
            #     bin[j] = 0
            #
            # # Store position of the bit set
            # # so that this bit and bits
            # # before it are not changed next time.
            # last_final = i + 1

    # Find decimal equivalent
    # of modified bin[]
    if changes == 0:
        bin_rep[position - 1] = 1
        bin_rep[position - 2] = 0
        bin_rep[position - 3] = 0
        bin_rep[0] = 1
    ans = 0
    for v in range(position):
        ans += bin_rep[v] * (1 << v)
    return ans


def countsetbits(k):
    count = 0
    while k:
        k &= (k - 1)
        count += 1
    return count


# Program to test function countSetBits
# i = 18432
# print(countSetBits(i))

# This code is contributed by
# Smitha Dinesh Semwal

def nth_sparse(p):
    if p == 1:
        return 3
    count = 1
    num = 3
    while count < p:
        num = nextsparse(num)  #
        if is_sparse(num):
            count += 1
    return num


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

while True:
    n = int(input())
    a = []

    for i in range(n):
        a.append(int(input()))
    # print(a)

    data = a
    # print(data)
    result = []
    for i in data:
        result.append(nth_sparse(i) % 35184372089371)
    print(*result, sep='\n')
