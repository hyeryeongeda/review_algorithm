n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = sum(arr[:m]) # 첫 번째 윈도우의 합
max_v = sum_v
max_idx = 0

# 슬라이딩 윈도우 기법
for i in range(n-m):
    # 1. 다음 윈도우 계산
    sum_v -= arr[i] # 첫 번째 값 빼고
    sum_v += arr[i+m] # 마지막 값 더하고

    # 2. 최대값 갱신
    if sum_v > max_v:
        max_v = sum_v
        max_idx = i + 1 # i가 현재 윈도우니까 i + 1이 다음 윈도우

print(max_idx)