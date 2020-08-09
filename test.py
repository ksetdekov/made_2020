# Python3 program to find next
# sparse number

def nextSparse(x):
    # Find binary representation of
    # x and store it in bin[].
    # bin[0] contains least significant
    # bit (LSB), next bit is in bin[1],
    # and so on.
    bin = []
    while (x != 0):
        bin.append(x & 1)
        x >>= 1

    # There my be extra bit in result,
    # so add one extra bit
    bin.append(0)
    n = len(bin)  # Size of binary representation

    # The position till which all
    # bits are finalized
    changes = 0

    # Start from second bit (next to LSB)
    for i in range(0, n - 2):

        # If current bit and its previous
        # bit are 1, but next bit is not 1.
        if bin[i] == 1 and bin[i + 1] != 1:
            # Make the next bit 1
            bin[i + 1] = 1
            bin[i] = 0
            changes+=1

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
        bin[n-1]=1
        bin[n-2]=0
        bin[n-3]=0
        bin[0] = 1
    ans = 0
    for i in range(n):
        ans += bin[i] * (1 << i)
    print(changes)
    return ans


# Driver Code
if __name__ == '__main__':
    x = 12
    print("Next Sparse Number is", nextSparse(x))
    print("{0:b}".format(3))
    print("{0:b}".format(5))
    print("{0:b}".format(6))
    print("{0:b}".format(9))

# This code is contributed by
# mits
