from itertools import permutations
import copy


def calculate(N_list, o_list):
    o_list = list(o_list)
    while o_list:
        a = N_list.pop(0)
        b = N_list.pop(0)
        o = o_list.pop(0)
        n = 0
        if o == '+':
            n = a + b
        elif o == '-':
            n = a - b
        elif o == '*':
            if a * b < 0:
                n = abs(a) * abs(b)
                n = n * -1
            else:
                n = a * b
        else:
            if a * b < 0:
                n = abs(a) // abs(b)
                n = n * -1
            else:
                n = a // b
        N_list.insert(0, n)
    return N_list[0]


if __name__ == "__main__":
    N = int(input())
    n_list = list(map(int, input().split()))
    P, M, m, d = map(int, input().split())
    P = '+' * P
    M = '-' * M
    m = '*' * m
    d = '/' * d
    o_list = P + M + m + d
    o_set = set(permutations(o_list))

    answer_lst = []
    while o_set:
        o = o_set.pop()
        answer = calculate(copy.deepcopy(n_list), o)
        answer_lst.append(answer)
    answer_lst.sort()
    print(answer_lst[-1])
    print(answer_lst[0])
