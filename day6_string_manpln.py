"""
Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as
2 space-separated strings on a single line 
(see the Sample below for more detail).
Note: 0 is considered to be an even index.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak

"""

n = int(input())

# strings = [(input('Enter a string: ')) for i in range(n)]

strings = []
for i in range(n):
    strings.append(input())
    
for s in strings:
    out1 = ''
    out2 = ''
    for j in range(len(s)):
        if j % 2 == 0:
            out1 += s[j]
        else:
            out2 += s[j]    
    print(f"{out1} {out2}")