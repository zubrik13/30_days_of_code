class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        low = min(self.__elements)
        high = max(self.__elements)
        self.maximumDifference = abs(low - high)
        return self.maximumDifference


# _ = input()
# a = [int(e) for e in input().split(' ')]

a = [1, 2, 5]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)