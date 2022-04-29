from copy import deepcopy
from itertools import product
from collections import defaultdict

dic=defaultdict(int)
dic['L']=(0,-1)
dic['R']=(0,1)
dic['U']=(-1,0)
dic['D']=(1,0)
ONE=[('L'),('R'),('U'),('D')]
TWO=[('L','R'),('U','D')]
THREE=[('U','R'),('R','D'),('D','L'),('L','U')]
FOUR=[('U','R','L'),('U','R','D'),('R','D','L'),('U','L','D')]
FIVE=[('U','R','D','L')]

def visit(board,orient_lst,c_x,c_y): #(L,R) board와 방향,현재위치 주면 #으로 만들어준다.
    for ori in orient_lst:  #ori==L OR ori==R
        dx = dic[ori][0]
        dy = dic[ori][1]
        nx=c_x+dx
        ny=c_y+dy
        while True:
            if nx<0 or R_N<=nx or ny<0 or C_N<=ny or board[nx][ny]==6:
                break
            else:
                if board[nx][ny]==0:
                    board[nx][ny]='#'
            nx+=dx
            ny+=dy
    return
def solution(board,dot_lst,comb_lst):
    answer=0
    for cur_location,ori_lst in zip(dot_lst,comb_lst):
        visit(board, ori_lst, cur_location[0],cur_location[1])
    for i in range(R_N):
        for j in range(C_N):
            if board[i][j]==0:
                answer+=1
    return answer

if __name__=="__main__":
    answer=float('inf')
    board=[]
    R_N,C_N=map(int,input().split())
    for _ in range(R_N):
        board.append(list(map(int,input().split())))
    comb_lst=[]
    dot_lst=[]
    for i in range(R_N):
        for j in range(C_N):
            if board[i][j]==1:
                comb_lst.append(ONE)
                dot_lst.append((i,j))
            elif board[i][j]==2:
                comb_lst.append(TWO)
                dot_lst.append((i,j))
            elif board[i][j] == 3:
                comb_lst.append(THREE)
                dot_lst.append((i,j))
            elif board[i][j] == 4:
                comb_lst.append(FOUR)
                dot_lst.append((i,j))
            elif board[i][j] == 5:
                comb_lst.append(FIVE)
                dot_lst.append((i,j))
            else:
                continue
    comb_lst=list(product(*comb_lst))   #신의한수..
    for c in comb_lst:
        sub_board=deepcopy(board)
        answer=min(solution(sub_board,dot_lst,c),answer)
    print(answer)
