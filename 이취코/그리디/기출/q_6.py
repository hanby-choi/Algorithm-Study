# 그리디 - 6. 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # 음식 섭취 시간, 음식 번호 
    cur_sum = 0 # 지금까지 먹은 시간
    past_food = 0 # 직전까지 먹은 음식의 food_times
    all_cnt = len(q) # 큐에 남아있는 음식의 총 수
    
    while cur_sum + (q[0][0] - past_food) * all_cnt <= k:
        now_food = heapq.heappop(q)
        cur_sum += (now_food[0] - past_food) * all_cnt
        all_cnt -= 1
        past_food = now_food[0]
    
    result = sorted(q, key=lambda x: x[1])
    return result[(k-cur_sum) % all_cnt][1]