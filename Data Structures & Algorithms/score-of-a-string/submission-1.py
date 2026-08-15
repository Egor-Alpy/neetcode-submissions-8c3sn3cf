class Solution:
    def scoreOfString(self, s: str) -> int:
        summa = 0
        for i in range(len(s)-1):
            summa += abs(ord(s[i+1]) - ord(s[i]))
        return summa