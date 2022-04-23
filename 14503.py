WALL=1
EMPTY=0
CLEANN=-1
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def clean(board,c_r,c_c,orient):
    board[c_r][c_c]=CLEANN
    answer=1
    while True:
        flag=0
        for _ in range(4):
            orient = (orient + 3) % 4
            nx=c_r+dx[orient]
            ny=c_c+dy[orient]
            if 0<=nx<R and 0<=ny<C and board[nx][ny]==EMPTY:
                answer+=1
                board[nx][ny]=CLEANN
                flag=1
                c_r,c_c=nx,ny
                break
        if not flag:
            if board[c_r-dx[orient]][c_c-dy[orient]]==WALL:
                break
            else:
                c_r=c_r-dx[orient]
                c_c=c_c-dy[orient]
    return answer

# 4바퀴 돌면서
# 만약 빈칸이면 가고
# 빈칸이 없으면 후진한다.
# 벽이면 나오고.
# for
if __name__=="__main__":
    R,C=map(int,input().split())
    cur_x,cur_y,orient=map(int,input().split())
    board=[]
    for _ in range(R):
        sub_lst=list(map(int,input().split()))
        board.append(sub_lst)
    answer=clean(board,cur_x,cur_y,orient)
    print(answer)