from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    priorities.sort()
    answer = 0
    while True:
        if q[0] == priorities[-1]:
            answer += 1
            q.popleft()
            priorities.pop()
            if location == 0:
                break
        else:
            q.append(q.popleft())
        location = len(q) - 1 if location == 0 else location-1
    return answer