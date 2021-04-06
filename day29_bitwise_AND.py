def bitwiseAnd(n, k):
    """
    A method that performs bitwise AND operation for all possible combinations A and B in set S,
    so that A < B
    :param N: set of values , int
    :param K: given limit , int
    :return: max value of AND operation, so that max(A&B) < K, int
    """
    # s = [int(i) for i in range(1, N + 1)]
    size = n
    lim = k
    max_ = 0
    for i in range(lim - 2, size + 1):
        for j in range(i + 1, size + 1):
            and_ = i & j

            if and_ == lim - 1:
                return and_

            if lim > and_ > max_:
                max_ = and_

    return max_


N = 8
K = 5

print(bitwiseAnd(N, K))
