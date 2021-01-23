def checkBalanceParenthesis(parList):
    parDict = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in parList:
        if char in parDict.values():
            stack.append(char)
        else:
            if not stack:
                return False
            peek = stack.pop()
            if peek != parDict[char]:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


parList = ["[]{[[{()}]]})", "[](){}{}()[]", "({[[{())(((()}]]})", "({[[{(}})))}]]})", "{([])}", "{{(({{", "}}}"]
for elem in parList:
    if checkBalanceParenthesis(elem):
        print("Balanced")
    else:
        print("Not Balanced")
