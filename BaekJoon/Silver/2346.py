from collections import deque

n = int(input())
queue = deque(list(enumerate(map(int, input().split()))))
answer = []

while queue:
    idx, num = queue.popleft()
    answer.append(idx+1)

    if num > 0:
        queue.rotate(-(num-1))
    else:
        queue.rotate(-num)

for i in answer:
    print(i, end=" ")