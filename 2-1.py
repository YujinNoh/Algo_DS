# 정렬된 리스트에 원소 삽입
def solution(L, x):
    for idx, num in enumerate(L):
        if num>=x:
            L.insert(idx,x)
            break
        if L[-1] < x:
            L.append(x)
    return L