def delim(c):
    return c==' '

def is_op(c):
    return c in ['+','-','*','/','%','^']

def priority(x):
    op,unary=x
    if unary:
        return 4
    elif op in ['+','-']:
        return 1
    elif op in ['*','/','%']:
        return 2
    else:
        return -1

def process_op(st,x):
    op,unary=x
    if unary:
        l=st.pop()
        if op=='+':
            st.append(l)
        elif op=='-':
            st.append(-l)
    else:
        r,l=st.pop(),st.pop()
        if op=='+':
            st.append(l+r)
        elif op=='-':
            st.append(l-r)
        elif op=='*':
            st.append(l*r)
        elif op=='/':
            st.append(l/r)
        elif op=='%':
            st.append(l%r)
        elif op=='^':
            st.append(pow(l,r))

def get_variable_var(op):
    if op=='g':
        return 42
    else:
        return 0

def isunary(op):
    return op in ['+','-']

def left_assoc(x):
    op,unary=x
    return not (unary or op=='^')

def calc(s):
    may_unary=True
    st,op=[],[]
    for i in range(len(s)):
        if not delim(s[i]):
            if s[i]=='(':
                op.append(('(',False))
                may_unary=True
            elif s[i]==')':
                while op[-1][0]!='(':
                    process_op(st,op.pop())
                op.pop()
                may_unary=False
            elif is_op(s[i]):
                curop,unary=s[i],False
                if may_unary and isunary(curop):
                    unary=True
                while op and \
                      (left_assoc((curop,unary)) and priority(op[-1])>=priority((curop,unary)) or \
                       not left_assoc((curop,unary)) and priority(op[-1])>priority((curop,unary))):
                    process_op(st,op.pop())
                op.append((curop,unary))
                may_unary=True
            else:
                operand=""
                while i<len(s) and s[i].isalnum():
                    operand+=s[i]
                    i+=1
                i-=1
                if operand[0].isdigit():
                    st.append(int(operand))
                else:
                    st.append(get_variable_var(operand))
                may_unary=False
    while op:
        process_op(st,op.pop())
    return st[-1]

assert calc("(4 + 3) * 6") == 42
assert calc("4 + 3 * 6") == 22
assert calc("g - 2") == 40
assert calc("x - 2") == -2
assert calc("-3+1") == -2
assert calc("1+(-3)") == -2
assert calc("+3+1") == 4
assert calc("2^3^4") == calc("2^(3^4)")
