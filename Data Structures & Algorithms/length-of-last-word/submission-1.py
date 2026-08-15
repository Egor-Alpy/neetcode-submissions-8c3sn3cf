class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        last_word = s_list[-1]
        len_last_word = len(last_word)
        return(len_last_word)