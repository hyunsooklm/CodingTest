from collections import deque
visit=set([])
def prunning(history):
    prun=False
    if history=='0':
        return prun
    for v in visit:
        #0145 015 02 0345 035 045 -> 015 in 0145, 035 in 0345 045 in 0145 or 045 in  0345
        n=0
        for s in history:
            if s not in v:
                break
            else:
                n+=1
        if n==len(history):
            prun=True
            break
    return prun

def dfs(N,T_list,P_list):
    stack=deque([])
    maxnum=0
    stack.append([0,0,'0'])
    while stack:
        day,total,history=stack.pop()
        print(f'day:{day} history:{history},maxnum:{maxnum}')
        if prunning(history):
            continue
        visit.add(history)  # 뻗어나갈 준비가 되있는 상태
        if day+T_list[day]<N+1:
            for n in range(day+T_list[day],N+1):
                if n+T_list[n]-1<=N:#해당일에 근무할 수 있다면
                    subsum=total+P_list[n]
                    new_history=history+str(n)
                    maxnum = max(maxnum, subsum)
                    print(f'subsum:{subsum},new_history:{new_history}')
                    stack.append([n,subsum,new_history])
    return maxnum
if __name__=='__main__':
    N=int(input())
    T_list=[1]  #0도 있으니까
    P_list=[0]
    for _ in range(N):
        T,P=map(int,input().split())
        T_list.append(T)
        P_list.append(P)
    print(f'T_list:{T_list}, P_list:{P_list}')
    answer=dfs(N,T_list,P_list)
    print(answer)