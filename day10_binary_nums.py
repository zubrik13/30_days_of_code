def numCounter(n):
    inp = str(bin(n))
    bnr = inp[2:]
    nums = bnr.split('0')
    count = []
    for num in nums:
        count.append(len(num))

    return max(count)


n = 439
print(numCounter(n))
