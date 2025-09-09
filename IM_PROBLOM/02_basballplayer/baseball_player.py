def bb_player(N,K,arr):
    arr.sort()
    left, right = 0, 0
    ret = 0
    
    while left < N and right< N:
        if arr[right] - arr[left] > K:
            left += 1
        else:
            right+=1
        ret = max(right-left,ret)
    return ret

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = bb_player(N,K,arr)
    print(f'#{tc} {result}')