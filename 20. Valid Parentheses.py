# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


## Hint: Remember Finite State Automata? What data structure did we use for this type of problem?
## Hint: How can we create a relationship btwn opening and closing parens?

### Hint: Use a stack to hold opening parens.
### Hint: Pop the top when encountering a close paren.
### Hint: Use a dictionary to hold closing : opening pairs.


# SOLUTION #
def validParen(s):
    stack = []
    paren = {"]":"[", "}":"{", ")": "("}

    for each in s:
        if each in paren and stack:
            top = stack.pop()
            if paren[each] != top:
                return False
        else:
            stack.append(each)
    return not stack

print(validParen("{[]}"))
print(validParen("()[]{}"))
print(validParen("({{{{}}}))"))
# SOLUTION #
