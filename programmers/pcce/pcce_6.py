def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

print(solution([3,4],[85,93],[85, 92, 38, 93, 48, 85, 92, 56]))