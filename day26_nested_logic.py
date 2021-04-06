from datetime import datetime


def fines(l):
    """
    A method, that calculates fines, given the expected and actual return dates for a library book
    :param l: list of lists with separated expected and return dates
    in following format [['dd', 'mm', 'yyyy'], ['dd', 'mm', 'yyyy']], data type - str
    :return: fine amount, int
    """
    lrd = [int(i) for i in l[0]]
    ldd = [int(i) for i in l[1]]
    return_date = datetime(year=lrd[2], month=lrd[1], day=lrd[0])
    due_date = datetime(year=ldd[2], month=ldd[1], day=ldd[0])
    days_diff = (return_date - due_date).days
    month_diff = lrd[1] - ldd[1]
    year_diff = lrd[2] - ldd[2]

    # print(return_date, due_date, days_diff, sep="\n")
    if days_diff <= 0:
        return 0
    elif year_diff > 0:
        return 10000
    elif year_diff == 0 and month_diff > 0:
        return 500 * month_diff
    else:
        return 15 * days_diff


# inputs = [(input().split()) for i in range(2)]

inputs = [['9', '6', '2015'], ['6', '6', '2015']]
i = [['31', '12', '2014'], ['1', '1', '2015']]

print(fines(inputs))
print(fines(i))
