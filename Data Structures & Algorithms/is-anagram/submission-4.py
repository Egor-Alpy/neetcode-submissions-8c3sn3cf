class Solution:
    def isAnagram(self, s_string: str, t_string: str) -> bool:

        if len(s_string) != len(t_string):
            return False

        s_list = list(s_string)
        t_list = list(t_string)

        for letter_s in s_list:
            
            print(f"s: {letter_s}")
            if letter_s in t_list:
                t_list.remove(letter_s)
            else:
                return False
        print(list(t_list))

        return t_list == []
