def solution(s):
    answer = 0
    str_list = list(s)
    i = 0
    
    while i < len(str_list) - 1 :
        if str_list[i] == str_list[i+1] :
            del str_list[i:i+2]
            i = max(0,i-1)
        else :
            i+=1
            
    if len(str_list) == 0:
       answer =1
        
    return answer

s = "baabaa"
print(solution(s))