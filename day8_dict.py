# n = int(input())

# inputs = [(input().split()) for i in range(n)]
# inputs2 = []

# while True:
#     try:
#         inputs2.append(input())
#     except EOFError:
#         break

inputs = [['sam', '99912222'], ['tom', '11122222'], ['harry', '12299933']]
inputs2 = ['sam', 'edward', 'harry']

names = []
nums = []

for i in range(len(inputs)):
    for j in range(len(inputs[i])): 
        if j == 0:
            names.append(inputs[i][j])
        else:
            nums.append(inputs[i][j])

d = dict(zip(names, nums))

for i in inputs2:
    if i in d.keys():
        print(f"{i}={d[i]}")
    else:
        print("Not found")
