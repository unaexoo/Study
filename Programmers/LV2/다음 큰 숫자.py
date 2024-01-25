def solution(n):
    answer = 0
    x = n + 1
    x_cnt= 0 
    n_cnt = bin(n).count('1')
    
    while True : 
        x_cnt = bin(x).count('1')
        if n_cnt == x_cnt :
            answer = x
            break
        x += 1
    return answer

n = 78
print(solution(n))