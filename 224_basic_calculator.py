# start of mine
class Solution:
    def is_number(self, i: int):
        if i <= '9' and i >= '0':
            return True
        return False

    def cmp(self, num: list, cal: list):
        if len(num) < 2:
            return
        if cal == []:
            return
        c = cal.pop()
        num2 = num.pop()
        num1 = num.pop()
        if c == '+':
            num.append(num1 + num2)
        else:
            num.append(num1 - num2)
        return

    def calculate(self, s: str) -> int:
        num = []
        cal = []
        long_int = False
        compute_flag = False
        for i in range(len(s)):
            if self.is_number(s[i]):
                if long_int == False:
                    num.append(int(s[i]))
                    long_int = True
                elif long_int == True:
                    temp_int = num[-1] * 10 + int(s[i])
                    num.pop()
                    num.append(temp_int)
            elif s[i] == ' ':
                long_int = False
                continue
            elif s[i] == '+' or s[i] == '-':
                long_int = False
                if compute_flag == True:
                    self.cmp(num, cal)
                compute_flag = True
                cal.append(s[i])
            elif s[i] == '(':
                compute_flag = False
            else:
                self.cmp(num, cal)
        self.cmp(num, cal)
        return num.pop()


# second method
def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    s = ''.join(s.split())
    for i in s+'+':
        if i.isdigit():
            num = 10 * num + int(i)
        elif i in '+-':
            res += num * sign * stack[-1]
            sign = 1 if i == '+' else -1
            num = 0
        elif i == '(':
            stack.append(sign * stack[-1])
            sign = 1
        elif i == ')':
            res += num * sign * stack[-1]
            num = 0
            stack.pop()
    return res


# third method
class Solution:
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-1'],
            elif c == ')':
                signs.pop()
            i += 1
        return total















