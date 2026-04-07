""" Validating Nested Structures (Compiler Design)
The Problem:
Compilers must verify that code like if(a[i] == {b: (1+2)}) is syntactically correct. Brackets must be closed in the exact reverse order they were opened, and types must match.

The Solution: The Expression Stack

Logic:

Scan the string from left to right.

If you see an opening tag (, [, or {, push it onto the stack.

If you see a closing tag, pop the top of the stack.

The Match Check: If the popped tag doesn't match the closing tag (e.g., popped { but saw ]), the code is invalid.

If the stack is not empty at the end, there’s an unclosed bracket. """

"Code : "

def is_valid_syntax(code):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in code:
        if char in mapping.values(): # Opening bracket
            stack.append(char)
        elif char in mapping.keys(): # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0
