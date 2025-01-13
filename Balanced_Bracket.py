def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "NO"
        else:
            return "NO"
    
    return "YES" if not stack else "NO"


if __name__ == "__main__":
    t = int(input())
    results = []
    for _ in range(t):
        s = input().strip()
        results.append(isBalanced(s))
    

    for result in results:
        print(result)
