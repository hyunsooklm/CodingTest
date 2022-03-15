from collections import deque
from copy import deepcopy
orient_lst=['U','D','L','R']
def move(arr,N,orient='R'):
    change=False
    if orient=='U':
        for y in range(N):
            for x in range(1,N):
                if not arr[x][y][0]:
                    continue    #빈칸이면 continue
                #끝이 빈칸이다. -> 데려오기.
                #끝이 빈칸이 아니다. -> 같거나 / 다르거나
                if arr[0][y][0]==0: #끝이 빈칸이다.
                    arr[0][y],arr[x][y]=arr[x][y],arr[0][y]
                    change=True
                else:
                    space=1
                    while(arr[x-space][y][0]==0):
                        space+=1
                   #arr[x-i][y]는 0이 아닌 곳
                    if arr[x-space][y][0]==arr[x][y][0] and not arr[x-space][y][1]:#같다면 합치고
                        arr[x-space][y][0]*=2
                        arr[x-space][y][1]=1
                        arr[x][y][0]=0
                        change=True
                    else:   #한칸 뒤에 넣어준다.
                        if space!=1:
                            change=True
                            arr[x-space+1][y],arr[x][y]=arr[x][y],arr[x-space+1][y]
    elif orient=='D':
        for y in range(N):
            for x in range(N-2,-1,-1):
                if not arr[x][y][0]:
                    continue    #빈칸이면 continue
                # 끝이 빈칸이다. -> 데려오기.
                # 끝이 빈칸이 아니다. -> 같거나 / 다르거나
                else:
                    if arr[N-1][y][0] == 0:  # 끝이 빈칸이다.
                        arr[N-1][y], arr[x][y] = arr[x][y], arr[N-1][y]
                        change = True
                    else:
                        space = 1
                        while (arr[x + space][y][0] == 0):
                            space += 1
                        # arr[x+space][y]는 0이 아닌 곳
                        if arr[x + space][y][0] == arr[x][y][0] and not arr[x + space][y][1]:  # 같다면 합치고
                            arr[x + space][y][0] *= 2
                            arr[x + space][y][1] = 1
                            arr[x][y][0] = 0
                            change = True
                        else:  # 한칸 뒤에 넣어준다.
                            if space != 1:
                                change = True
                                arr[x + space - 1][y], arr[x][y] = arr[x][y], arr[x + space - 1][y]
    elif orient=='L':
        for x in range(N):
            for y in range(1,N):
                if not arr[x][y][0]:
                    continue
                #끝이 빈칸이다. -> 데려오기.
                #끝이 빈칸이 아니다. -> 같거나 / 다르거나
                if arr[x][0][0]==0: #끝이 빈칸이다.
                    arr[x][0],arr[x][y]=arr[x][y],arr[x][0]
                    change=True
                else:
                    space=1
                    while(arr[x][y-space][0]==0):
                        space+=1
                   #arr[x-i][y]는 0이 아닌 곳
                    if arr[x][y-space][0]==arr[x][y][0] and not arr[x][y-space][1]:#같다면 합치고
                        arr[x][y-space][0]*=2
                        arr[x][y-space][1]=1
                        arr[x][y][0]=0
                        change=True
                    else:   #한칸 뒤에 넣어준다.
                        if space!=1:
                            change=True
                            arr[x][y-space+1],arr[x][y]=arr[x][y],arr[x][y-space+1]
    else:
        for x in range(N):
            for y in range(N-2,-1,-1):
                if not arr[x][y][0]:
                    continue
                if arr[x][N-1][0]==0: #끝이 빈칸이다.
                    arr[x][N-1],arr[x][y]=arr[x][y],arr[x][N-1]
                    change=True
                else:
                    space=1
                    while(arr[x][y+space][0]==0):
                        space+=1
                    if arr[x][y+space][0]==arr[x][y][0] and not arr[x][y+space][1]:#같다면 합치고
                        arr[x][y+space][0]*=2
                        arr[x][y+space][1]=1
                        arr[x][y][0]=0
                        change=True
                    else:   #한칸 뒤에 넣어준다.
                        if space!=1:
                            change=True
                            arr[x][y+space-1],arr[x][y]=arr[x][y],arr[x][y+space-1]

    return arr,change

def calculator(arr):
    answer=-1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                if answer<arr[i][j][0]:
                    answer=arr[i][j][0]
    return answer

def dfs(arr):
    answer=calculator(arr)
    stack=deque([])
    stack.append([arr,0])
    while stack:
        new_arr,depth=stack.pop()
        for o in orient_lst:
            result_arr,result=move(deepcopy(new_arr),len(new_arr),o)
            if result:
                result_arr=[[[result_arr[r][c][0],0] for c in range(len(arr))] for r in range(len(arr[0]))]
                max_num=calculator(result_arr)
                answer=max(max_num,answer)
                if depth<4:
                    stack.append([result_arr,depth+1])
    return answer
if __name__=='__main__':
    N=int(input())
    arr=[[[0,0] for _ in range(N)] for _ in range(N)]
    arr=[]
    for _ in range(N):
        lst=list(map(int,input().split()))
        new_lst=[[l,0] for l in lst]
        arr.append(new_lst)
    answer=dfs(arr)
    print(answer)