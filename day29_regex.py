import math
import os
import random
import re
import sys

if __name__ == '__main__':

    def is_gmail(email):
        if email[1] == 'gmail.com':
            return True


    # N = int(input())
    N = 6
    names = ['riya', 'julia', 'julia', 'julia', 'samantha', 'tanya']
    emails = ['riya@gmail.com', 'julia@gmail.com', 'sjulia@gmail.com',
             'julia@gmail.com', 'samantha@gmail.com', 'tanya@gmail.com']


    gmail = []
    for N_itr in range(N):
        # firstNameEmailID = input().split()
        # firstName = firstNameEmailID[0]
        # emailID = firstNameEmailID[1]

        # firstNameEmailID = input().split()
        firstName = names[N_itr]
        emailID = emails[N_itr]
        email = re.split(r'@', emailID)

        if is_gmail(email):
            gmail.append(firstName)

    out = sorted(gmail)
    print(*out, sep="\n")
