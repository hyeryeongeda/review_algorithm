arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

idx = int(input())  # 사용자에게 시작 인덱스를 입력받음 (0 이상 6 이하)

def get_sum(idx):
    sum_v = 0
    # idx부터 시작해서 연속된 5개의 값을 더한다
    for i in range(5):
        sum_v += arr[idx + i]  # arr[idx], arr[idx+1], ..., arr[idx+4]
    return sum_v

# get_sum 함수 실행 결과(연속 5개 합)를 출력
print(get_sum(idx))