class Solution(object):
    def addDigits(self, num):
        
        
        while num > 9:
            summary = 0
            while num > 0:
                summary = summary + num % 10
                num = int(num/10)
            num = num + summary
        print(num)

num = 9999999999999
test_solution = Solution()
test_solution.addDigits(num)