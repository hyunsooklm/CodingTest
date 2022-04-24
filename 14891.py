from collections import deque
def rotate(lst,orient):
    if orient==1:# 톱니바퀴인경우
        return [lst[-1]]+lst[0:-1]
    elif orient==-1:
        return lst[1:]+[lst[0]]
    else:
        print("??")
def solution(top_lst):
    answer=0
    for index,l in enumerate(top_lst):
        if index==0:
            if l[0]==1:
                answer+=1
        elif index==1:
            if l[0]==1:
                answer+=2
        elif index==2:
            if l[0]==1:
                answer+=4
        else:
            if l[0]==1:
                answer+=8
    return answer

def calculate(toblst,index,orient):
    circled=[False for _ in range(4)]
    queue=deque([])
    queue.append([index,orient])
    while queue:
        index,orient=queue.popleft()    #target 톱니바퀴의 번호는?
        if index==0:    #맨 왼쪽 돌려야하면
            if not circled[index+1]:
                if toblst[index][2]!=toblst[index+1][6]:    #다른 극
                    if orient==1:
                        queue.append([index+1,-1])
                    elif orient==-1:
                        queue.append([index+1,1])
                    #오른쪽 확인  & queue에 번호와 방향 넣기

        elif index==3:  #맨 오른쪽 돌려야하면
            if not circled[index-1]:    #왼쪽 아직 안돌아갔으면
                if toblst[index-1][2]!=toblst[index][6]:    #다른 극
                    if orient==1:
                        queue.append([index-1,-1])
                    elif orient==-1:
                        queue.append([index - 1, 1])
                    # 왼쪽 확인 & queue에 번호와 방향 넣기

        else:   #중간이면
            if not circled[index-1]:    #왼쪽 아직 안돌아갔으면
                if toblst[index-1][2]!=toblst[index][6]:    #다른 극
                    if orient == 1:
                        queue.append([index - 1, -1])
                    elif orient == -1:
                        queue.append([index - 1, 1])
                    # 왼쪽 확인 & queue에 번호와 방향 넣기

            if not circled[index+1]:
                if toblst[index][2]!=toblst[index+1][6]:    #다른 극
                    if orient==1:
                        queue.append([index+1,-1])
                    elif orient==-1:
                        queue.append([index + 1, 1])
                    #오른쪽 확인  & queue에 번호와 방향 넣기
        toblst[index]=rotate(toblst[index],orient)
        circled[index]=True
        #돌리고 circled에 표시
    return toblst
if __name__=="__main__":
    tob_lst=[]
    for _ in range(4):
        tob_lst.append(list(map(int,list(input()))))
    K=int(input())
    target_lst=[]
    for index in range(K):
        N,Orient=map(int,input().split())
        tob_lst=calculate(tob_lst,N-1,Orient)
    print(solution(tob_lst))