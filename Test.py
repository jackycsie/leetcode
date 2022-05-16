class Solution:
    def calculate(self, s):

        queue_number = []
        currect_number = 0
        operation = 1
        register = 0

        for i in s:
            if i.isdigit():
                currect_number = currect_number * 10 + int(i)
            elif i == '+' or i == '-':
                register = register + currect_number * operation
                currect_number = 0
                operation = 1 if i == "+" else -1
            elif i == '(':
                queue_number.append(register)
                queue_number.append(operation)
                register = 0
                operation = 1
            elif i == ')':
                register = register + currect_number * operation
                currect_number = 0
                register = register * queue_number.pop()
                register = register - queue_number.pop()
                print(queue_number)
        register = register + currect_number * operation
        return register

s = "(1+(4+5+2)-3)+(6+8)"

test_solution = Solution()
test_solution.calculate(s)
