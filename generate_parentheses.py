def generate_parantheses(n):
    result = []
    backtrack("", 0, 0, n, result)
    return result

def backtrack(s, left, right, n, result):
    if len(s) == 2 * n:
        result.append(s)
        return
    if left < n:
        backtrack(s + "(", left + 1, right, n, result)
    if right < left:
        backtrack(s + ")", left, right + 1, n, result)

s = generate_parantheses(3)
# Expected output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
print(s)
