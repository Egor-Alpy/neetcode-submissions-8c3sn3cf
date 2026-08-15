class Solution:
    def countSeniors(self, details: List[str]) -> int:
        k = 0
        for detail in details:
            print(detail)
            age = int(detail[-4:-2])
            if age > 60:
                k += 1
        return k