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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for c in tokenList:
        if (c not in prec) and (c != ')'):
            postfixList.append(c)
        elif c == "(":
            opStack.push(c)
        elif c == ")":
            while str(opStack.peek()) != '(':
                postfixList.append(str(opStack.pop()))
            opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[c] &lt;= prec[str(opStack.peek())]):
                postfixList.append(str(opStack.pop()))
            opStack.push(c)
                    
    while not opStack.isEmpty():
        postfixList.append(str(opStack.pop()))  
     
    return postfixList

def postfixEval(tokenList):
    evalStack = ArrayStack()
    
    for c in tokenList:
        if isinstance(c, int):
            evalStack.push(c)
        else:
            data2 = evalStack.pop()
            data1 = evalStack.pop()
            if c == '+':
                val = data1 + data2
            elif c == '-':
                val = data1 - data2
            elif c == '*':
                val = data1 * data2
            else:
                val = data1 / data2
            evalStack.push(val)
        
    return evalStack.pop()



def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
