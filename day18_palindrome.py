class Solution:
    stack = []
    queue = []

    def pushCharacter(self, i):
        return self.stack.append(i)

    def enqueueCharacter(self, i):
        return self.queue.append(i)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        letter = self.queue[0]
        self.queue.remove(self.queue[0])
        return letter


# read the string s
# s = input()
s = "racecar"
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")


# simple solution w/o use of stacks and queues
def is_Palindrome(s):
    i = 0
    j = len(s) - 1
    res = f"The word, {s}, is not a palindrome."
    for step in range(len(s) // 2):
        if s[i] == s[j]:
            i += 1
            j -= 1
            res = f"The word, {s}, is a palindrome."
        else:
            return f"The word, {s}, is not a palindrome."
    return res


s = "racecar"
print(is_Palindrome(s))


# Very nice solution using Recursion
def is_palindrome(s):
    """
    Non-letters and capitalization are ignored
    :param s: str
    :return: True if letters in s form a palindrome; False otherwise
    """

    def to_chars(s):
        s = s.lower()
        letters = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                letters += char
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


print(is_palindrome(s))
