class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if (c not in prec) and (c != ')'):
            answer += c
        else:
            if c == ')':
                while str(opStack.peek()) != '(':
                    answer += str(opStack.pop())
                opStack.pop()
                
            elif c == '(':
                opStack.push(c)
            
            else:
                while (not opStack.isEmpty()) and (prec[c] <= prec[str(opStack.peek())]):
                    answer += str(opStack.pop())
                opStack.push(c)
                     
    while not opStack.isEmpty():
        answer += str(opStack.pop())
                
    return answer

