class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        for s_letter in s:
            if t != "":
                if t[0] == s_letter:
                    t = t[1::]
        print(t)
        return len(t)