def solution(board, h, w):
    n = len(board)
    count = 0
    dh =  [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(0,4): 
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if (0<= h_check and h_check < n) and 0 <= w_check and w_check < n:
            if board[h][w] == board[h_check][w_check] :
                count+=1
    return count

board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1

print(solution(board,h,w))