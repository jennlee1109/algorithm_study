s = input()
t = input()
stack = [t[i] for i in range(len(t))]

while len(s) < len(stack):
    if stack[-1] == 'A':
        stack.pop()
    else:
        stack.pop()
        stack.reverse()

if s == "".join(stack):
    print(1)
else:
    print(0)