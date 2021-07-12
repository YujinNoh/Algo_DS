# 이진 탐색 함수
def solution(L, x):
    answer = 0
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        mid = (lower + upper)//2
        if L[mid] < x:
            lower = mid + 1

        elif L[mid] > x:
            upper = mid - 1

        elif L[mid] == x:
            answer = mid
            break

    if lower > upper:
        answer = -1

    return answer