class Solution:
    def firstUniqChar(self, s):
        
        hasttable_tmp = {}
        for i in s:
            if i not in hasttable_tmp:
                hasttable_tmp[i] = 1
            else:
                hasttable_tmp[i] += 1

        min_count = hasttable_tmp[s[0]]
        Record_Position = 0
        for i in range(len(s)):
            if hasttable_tmp[s[i]] < min_count:
                min_count = hasttable_tmp[s[i]]
                Record_Position = i
        print(s[i])
        
s = "aabb"

test_solution = Solution()
test_solution.firstUniqChar(s)