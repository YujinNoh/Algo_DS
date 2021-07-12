# 리스트에서 원소 찾아내기
def solution(L, x):
    answer = []
    if x in L:
        for i, y in enumerate(L):
            if(y == x): 
                answer.append(i)
    else:
        answer.append(-1)
    return answer