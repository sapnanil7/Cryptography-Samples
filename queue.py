stack = []
top =0
def push(stack,value):
        stack[top] = value
        top=top+1
        return stack
def pop(stack):
        if top<0:
                retun -1
        value = stack[top]
        top=top -1
        return value


