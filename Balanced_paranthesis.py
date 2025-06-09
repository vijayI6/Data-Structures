expr = input()
pairs = {'{': '}', '[': ']', '(': ')'}
stack = []
for char in expr:
    if char in '([{':
        stack.append(char)
    elif char in '}])':
        if not stack or pairs[stack.pop()] != char:
            print('False')
            break
else:
    print(len(stack) == 0)

# Output:
# '(){}'
#  True
