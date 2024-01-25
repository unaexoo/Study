def solution(s):
    answer = 0
    stack = []
    
    for c in s :
        if stack and stack[-1] == c : 
            stack.pop()
        else :
            stack.append(c)
    
    if len(stack) == 0 :
        answer = 1  
    return answer

s = "baabaa"
print(solution(s))