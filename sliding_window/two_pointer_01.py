def get_idx():
    left = 0 # 왼쪽 포인터 (배열의 시작)
    right = len(arr) - 1 # 오른쪽 포인터 (배열의 끝)

    while left < right: # 두 포인터가 만나기 전까지 반복
        current_sum = arr[left] + arr[right] # 현재 합계

        if current_sum == m: # 현재 합이 타겟과 일치
            print(left, right)
            return

        elif current_sum < m: # 현재 합이 타겟보다 작으면
            left += 1 # 왼쪽 포인터를 오른쪽으로 이동(합을 키우기 위해)

        else:
            right -= 1 # 오른쪽 포인터를 왼쪽으로 이동 (합을 줄이기 위해)

    print('찾을 수 없음')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
get_idx()