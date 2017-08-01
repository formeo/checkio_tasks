def checkio(expression):
    if (expression.find('[') ==-1 and expression.find('{') ==-1 and expression.find('(') ==-1 and expression.find(']') ==-1 and expression.find('}') ==-1 and expression.find(')') ==-1):
        return True
    myl=list(expression)

    checkClose = list()
    for enum in myl:
        if enum == '(' or enum == '[' or enum == '{':
            checkClose.append(enum)
        if enum == ')' or enum == ']' or enum == '}':
            checkClose.append(enum)


    check = 0
    for x in range(len(checkClose)):
        if checkClose[x]=='[' and checkClose[x+1]!=']':
            check=1
        if checkClose[x]=='(' and checkClose[x+1]!=')':
            check=1
        if checkClose[x]=='{' and checkClose[x+1]!='}':
            check=1
    if check==0:
        return True

    closelist=list()
    openlist=list()
    for enum in myl:
        if enum == '(' or enum == '[' or  enum == '{':
           openlist.append(enum)
        if enum == ')' or enum == ']' or  enum == '}':
           closelist.append(enum)

    # print('openlist',openlist)
    # print('closelist', closelist)

    # print('openlist pop', openlist.pop())
    # print('closelist pop', closelist.pop(0))
    # print('openlist', openlist)
    # print('closelist', closelist)

    if len(openlist) ==0 and  len(closelist)==0:
        return True

    if len(openlist)!= len(closelist):
        return False

    maxLen=len(openlist)
    i=0

    while i<=maxLen-1:
        # print(i)

        ol= openlist.pop()
        cl=closelist.pop(0)


        if ol=='(' and cl!=')':
            return False

        if ol=='[' and cl!=']':
            return False

        if ol == '{' and cl != '}':
            return False

        i+=1


    return True
