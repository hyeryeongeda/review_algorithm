좋아, **개념 → 아주 작은 예제 → 살짝 확장 → 가지치기 추가** 순서로 딱 감 잡히게 보여줄게. (전부 파이썬)

---

# 0) 한 줄 요약

* **완전탐색(Brute Force)**: 가능한 모든 경우를 전부 시도.
* **가지치기(Pruning)**: “이 길은 답 불가”가 확실해지는 순간, 그 \*\*가지(경우)\*\*를 더 안 탐색하고 잘라냄.

---

# 1) 가장 작은 예제: 선형 탐색

## (1) 완전탐색

```python
arr = [1, 3, 7, 9, 11]
target = 9

found = False
for x in arr:              # 모든 원소를 '전부' 확인
    if x == target:
        found = True
        break
print(found)  # True
```

## (2) 가지치기 (정렬되어 있을 때만 가능)

```python
arr = [1, 3, 7, 9, 11]     # 오름차순 정렬
target = 8

found = False
for x in arr:
    if x == target:
        found = True
        break
    if x > target:         # 여기서 더 가도 절대 못 찾음 → 가지치기
        break
print(found)  # False
```

* 핵심: **정렬** 덕분에 “더 큰 값 나오면 끝”이라는 **근거**가 생김 → 가지치기 가능.

---

# 2) 두 수의 합 = T 찾기

## (1) 완전탐색 (모든 쌍 확인)

```python
arr = [1, 2, 3, 4, 5]
T = 6

pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == T:
            pairs.append((arr[i], arr[j]))
print(pairs)  # [(1,5), (2,4)]
```

## (2) 가지치기 (정렬 가정)

```python
arr = [1, 2, 3, 4, 5]   # 정렬되어 있다고 가정
T = 6

pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        s = arr[i] + arr[j]
        if s == T:
            pairs.append((arr[i], arr[j]))
        elif s > T:
            break  # j가 오른쪽으로 갈수록 더 커짐 → 이 i에선 더 볼 필요 없음 (가지치기)
print(pairs)
```

---

# 3) 모든 “문자열” 만들어보기 (완전탐색의 감 잡기)

## (1) 완전탐색: 길이 2, 알파벳 {A,B}로 가능한 모든 문자열

```python
chars = ['A', 'B']
res = []
for a in chars:
    for b in chars:
        res.append(a + b)
print(res)  # ['AA','AB','BA','BB']
```

## (2) 재귀로 일반화(길이 L)

```python
def gen_all(chars, L):
    out = []
    def dfs(cur):
        if len(cur) == L:          # 길이 도달 → 저장
            out.append(cur)
            return
        for ch in chars:           # 모든 선택 가보기 (완전탐색)
            dfs(cur + ch)
    dfs("")
    return out

print(gen_all(['A','B','C'], 2))  # ['AA','AB','AC','BA',...]
```

## (3) 가지치기: “연속해서 'AA' 금지”

```python
def gen_no_AA(chars, L):
    out = []
    def dfs(cur):
        if len(cur) >= 2 and cur[-2:] == "AA":
            return                 # 이 가지는 규칙 위반 → 잘라냄 (가지치기)
        if len(cur) == L:
            out.append(cur)
            return
        for ch in chars:
            dfs(cur + ch)
    dfs("")
    return out

print(gen_no_AA(['A','B'], 3))  # 'AA' 연속 없는 것만 나옴
```

---

# 4) 부분집합(Subset) 전수조사

## (1) 완전탐색: 비트마스크(반복문만으로 모든 부분집합)

```python
arr = [1,2,3]
subs = []
for mask in range(1 << len(arr)):      # 0..2^n-1
    subset = []
    for i in range(len(arr)):
        if mask & (1 << i):            # i번째 원소 포함?
            subset.append(arr[i])
    subs.append(subset)
print(subs)  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

## (2) 재귀 완전탐색(고른다/안 고른다)

```python
arr = [1,2,3]
res = []
def dfs(idx, chosen):
    if idx == len(arr):
        res.append(chosen[:])
        return
    # 1) arr[idx] 고름
    chosen.append(arr[idx])
    dfs(idx+1, chosen)
    chosen.pop()
    # 2) arr[idx] 안 고름
    dfs(idx+1, chosen)

dfs(0, [])
print(res)
```

## (3) 가지치기: “합이 10을 넘으면 더 깊이 X”

```python
arr = [1,2,3,4,5,6,7,8,9,10]
target = 10
ans = []

def dfs(idx, chosen, total):
    if total > target:              # 가지치기 1: 이미 초과
        return
    if idx == len(arr):
        if total == target:
            ans.append(chosen[:])
        return
    # 고름
    dfs(idx+1, chosen + [arr[idx]], total + arr[idx])
    # 안 고름
    dfs(idx+1, chosen, total)

dfs(0, [], 0)
for s in ans:
    print(*s)
```

*(더 진한 가지치기)*
남은 원소들을 전부 더해도 target에 못 미치면 중단 같은 “상한/하한”도 가능해요. (조금 진도 나간 뒤에 익히면 좋아요)

---

# 5) 제약 충족 예제: N-Queens(간단 버전)

완전탐색으로는 “모든 배치”를 다 시도.
가지치기는 “같은 열/대각선 충돌하면 더 진행 X”.

```python
N = 4
col_used = [False]*N
diag1 = set()  # r - c
diag2 = set()  # r + c
cnt = 0

def place(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for c in range(N):
        if col_used[c] or (row-c) in diag1 or (row+c) in diag2:
            continue   # 충돌 → 이 선택은 버림 (가지치기)
        col_used[c] = True
        diag1.add(row-c); diag2.add(row+c)
        place(row+1)
        col_used[c] = False
        diag1.remove(row-c); diag2.remove(row+c)

place(0)
print(cnt)  # 4-Queens 해의 개수: 2
```

* 여기서 **모든 칸**을 다 놓아보는 게 완전탐색,
* **충돌 검사로 바로 건너뛰는 것**이 가지치기.

---

## 마무리 요약

* 완전탐색은 “전부 시도”. 구현은 쉽고 확실하지만, 느릴 수 있음.
* 가지치기는 “가망 없는 분기 빨리 버리기”. **정렬, 제약(규칙), 상한/하한, 중간합** 같은 근거로 잘라냄.
* 위 예제들을 차례로 따라 해보면, 개념이 **코드로 어떻게 바뀌는지** 딱 감이 와요.

