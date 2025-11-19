history_stack = []
history_stack.append("Home Page")
history_stack.append("Products")
history_stack.append("Checkout")
print (history_stack[2])

def back(history_stack):
    history_stack.pop()
    return history_stack

back(history_stack);

print(history_stack)
    