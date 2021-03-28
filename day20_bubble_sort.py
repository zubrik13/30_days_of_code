def bubbleSort(lst):
    """
    Simple in memory sort, time complexity O((len(n))^2) - quadratical
    takes a list of integers as input
    """
    numSwaps = 0
    size = len(lst) - 1

    for i in range(size):
        for j in range(0, size - i):
            if lst[j+1] < lst[j]: # compare if the next item is smaller
                lst[j], lst[j+1] = lst[j+1], lst[j] # make a swap
                numSwaps += 1

    firstElement = lst[0]
    lastElement = lst[-1]

    string_1 = f"Array is sorted in {numSwaps} swaps."
    string_2 = f"First Element: {firstElement}"
    string_3 = f"Last Element: {lastElement}"
    print(string_1, string_2, string_3, sep="\n")


# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
a = [4, 3, 1, 2]
bubbleSort(a)
