def solution(board,dy,N,L):
    answer=0
    for i in range(N):  #줄단위
        flag=True
        for j in range(N-1):    #1줄 내에서
            if board[i][j]!=board[i][j+dy]: #앞 뒤 높이가 달라!
                height_diff=board[i][j]-board[i][j+dy]    #앞 뒤 높이차이
                if abs(height_diff)>1:  #1이상
                    flag=False
                    break
                if height_diff==-1: #앞이 뒤보다 낮으면
                    if j+dy-L<0 or visited[i][j]:    #다리놓을 공간도 안되면
                        flag=False
                        break
                    for k in range(1,L+1):  #j+dy-L ~ j+dy-1까지 경사로 놓을 수 있는가?
                        if visited[i][j+dy-(k*dy)] or board[i][j+dy-(k*dy)]-board[i][j+dy]!=height_diff:
                            #경사로를 놓을 공간에 이미 경사로가 있거나 높이가 1이상 차이날 경우
                            flag=False
                            break
                    for k in range(1,L+1):
                        visited[i][j+dy-(k*dy)]=True
                #경사로 놓아주기
                elif height_diff==1:    #앞이 뒤보다 높으면
                    if j + L >= N:  # 다리놓을 공간도 안되면
                        flag = False
                        break
                    for k in range(1, L + 1):  # j+dy-L ~ j+dy-1까지 경사로 놓을 수 있는가?
                        if visited[i][j + (k * dy)] or board[i][j]- board[i][j + (k * dy)] != height_diff:
                            # 경사로를 놓을 공간에 이미 경사로가 있거나 높이가 1이상 차이날 경우
                            flag = False
                            break
                    for k in range(1, L + 1):
                        visited[i][j + (k * dy)] = True
                    # 경사로 놓아주기
        for j in range(N):
            visited[i][j]=False
        if flag:
            answer+=1
    return answer
if __name__=="__main__":
    N,L=map(int,input().split())
    board=[]
    for _ in range(N):
        board.append(list(map(int,input().split())))
    visited=[[False for _ in range(N)] for _ in range(N)]
    sero_board=[]
    for l in zip(*board):
        sero_board.append(list(l))
    answer=solution(board,1,N,L)+solution(sero_board,1,N,L)
    print(answer)