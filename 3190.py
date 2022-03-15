from collections import defaultdict
from collections import deque
AppleSet={}
orient_dict = defaultdict(str)
orient_dict['SL'] = 'U'
orient_dict['SD'] = 'D'
orient_dict['UL'] = 'UL'
orient_dict['UD'] = 'UD'
orient_dict['DL'] = 'DL'
orient_dict['DD'] = 'DD'
orient_dict['ULL'] = 'D'
orient_dict['ULD'] = 'U'
orient_dict['UDL'] = 'U'
orient_dict['UDD'] = 'D'
orient_dict['DLL'] = 'U'
orient_dict['DLD'] = 'D'
orient_dict['DDL'] = 'D'
orient_dict['DDD'] = 'U'

def move(x,y,board,queue):
        if board[x][y] == True:  # 사과인경우
            board[x][y] = False
        else:  # 사과가 아니면
            queue.popleft()  # 꼬리 떼내기
        queue.append((x, y))

def calculate(move_lst,board,N):
    queue=deque([])
    queue.append((0,0))
    orient='S'
    time=0
    while True:
        time+=1
        x,y=queue[-1]   #머리
        if orient=='S' or orient=='UD' or orient=='DL':
            dx=0
            dy=1
            if x + dx < 0 or N <= x + dx or y + dy < 0 or N <= y + dy or (x + dx, y + dy) in queue:
                break
            else:
                x=x+dx
                y=y+dy
                move(x,y,board,queue)
        elif orient=='UL' or orient=='DD':
            dx=0
            dy=-1
            if x + dx < 0 or N <= x + dx or y + dy < 0 or N <= y + dy or (x + dx, y + dy) in queue:
                break
            else:
                x=x+dx
                y=y+dy
                move(x,y,board,queue)
        elif orient=='D':
            dx=+1
            dy=0
            if x + dx < 0 or N <= x + dx or y + dy < 0 or N <= y + dy or (x + dx, y + dy) in queue:
                break
            else:
                x=x+dx
                y=y+dy
                move(x,y,board,queue)
        elif orient=='U':
            dx=-1
            dy=0
            if x + dx < 0 or N <= x + dx or y + dy < 0 or N <= y + dy or (x + dx, y + dy) in queue:
                break
            else:
                x=x+dx
                y=y+dy
                move(x,y,board,queue)

        else:
            pass    #이런 경우 없음
        if move_lst and time==move_lst[0][0]:        #시간 되면 방향바꿔주기
            ori=move_lst[0][1]
            orient=orient_dict[orient+ori]  #방향바꿔주기
            move_lst.pop(0)
    return time
if __name__=='__main__':
    N=int(input())
    appleNum=int(input())
    board=[[False for _ in range(N)] for _ in range(N)]
    for _ in range(appleNum):
        x,y=map(int,input().split())
        board[x-1][y-1]=True
    moveNum=int(input())
    move_lst=[]
    for _ in range(moveNum):
        time,orient=input().split()
        move_lst.append((int(time),orient))
    answer=calculate(move_lst,board,N)
    print(answer)