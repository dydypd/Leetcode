class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0: 
            return True
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        
        return False


# Tạo một đối tượng của lớp Solution
solution_instance = Solution()

# In kết quả
print(solution_instance.isMatch("", ""))
print(solution_instance.isMatch("aa", "a*"))
print(solution_instance.isMatch("ab", "."))
print(solution_instance.isMatch("aab", "c*a*b"))
print(solution_instance.isMatch("mississippi", "mis*is*p*."))
print(solution_instance.isMatch("", ".*"))