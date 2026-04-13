class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for t_letter in t:
            if s != "":
                if s[0] == t_letter:
                    s = s[1::]
        if s == "":
            return True
        return False