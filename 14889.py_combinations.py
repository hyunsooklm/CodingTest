from itertools import combinations
if __name__=="__main__":
    N=int(input())
    board=[]
    for _ in range(N):
        sub_lst=list(map(int,input().split()))
        board.append(sub_lst)
    index_comb=list(combinations(list(range(N)),N//2))
    answer_lst=[]
    answer=float('inf')
    total_set=set(range(N))
    for A_comb in index_comb:
        A_set=set(A_comb)
        B_set=total_set-A_set
        A_lst=list(combinations(A_set,2))
        B_lst=list(combinations(B_set,2))
        A_total=0
        B_total=0
        for a,b in A_lst:
            A_total+=board[a][b]+board[b][a]
        for c,d in B_lst:
            B_total+=board[c][d]+board[d][c]
        answer=min(answer,abs(A_total-B_total))
        #1. 각 comb마다 2개씩 뽑아주고
        #결과값 나타내기
    print(answer)