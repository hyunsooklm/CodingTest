import copy
from itertools import combinations
from collections import deque
VIRUS=2
WALL=1
EMPTY=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(board):
    answer=0
    queue=deque([])
    for r in range(N):
        for c in range(M):
            if board[r][c]==VIRUS:
                queue.append([r,c])
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dx[i]
            nc=c+dy[i]
            if 0<=nr<N and 0<=nc<M and board[nr][nc]==EMPTY:
                board[nr][nc]=VIRUS
                queue.append([nr,nc])

    for r in range(N):
        for j in range(M):
            if board[r][j]==EMPTY:
                answer+=1
    return answer
if __name__=='__main__':
    answer=0
    N,M=map(int,input().split())
    board=[]
    virus_lst=deque([])
    empty_lst=deque([])
    for i in range(N):
        board.append(list(map(int,input().split())))
    for r in range(N):
        for c in range(M):
            if board[r][c]==EMPTY:
                empty_lst.append([r,c])
    candidate_lst=list(combinations(empty_lst,3))
    for a,b,c in candidate_lst:
        a_l,a_r=a
        b_l,b_r=b
        c_l,c_r=c
        sub_board=copy.deepcopy(board)
        sub_board[a_l][a_r] = WALL
        sub_board[b_l][b_r] = WALL
        sub_board[c_l][c_r] = WALL
        numwall=bfs(sub_board)
        answer=max(answer,numwall)
    print(len(candidate_lst))
    print(answer)