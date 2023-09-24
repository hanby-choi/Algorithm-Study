# 연산자 끼워넣기: 브루트포스, 백트래킹
def calc(mode, op1, op2):
    if mode == 0:
        return op1 + op2
    elif mode == 1:
        return op1 - op2
    elif mode == 2:
        return op1 * op2
    elif mode == 3:
        return int(op1 / op2)

def backtracking(value, index, n, operand, operator_cnt, ans): # 지금까지의 연산 값, 지금까지 연산한 피연산자 수, 전체 피연산자 수, 피연산자 배열, 연산자 수 배열, 현재까지 연산 최대/최소값 
        if index == n:
            ans[0] = max(ans[0], value)
            ans[1] = min(ans[1], value)
            return
        for mode in range(4):
             if operator_cnt[mode] > 0:
                  operator_cnt[mode] -= 1
                  next_value = calc(mode, value, operand(index))
                  backtracking(next_value, index+1, n, operand, operator_cnt, ans)
                  operator_cnt[mode] += 1

def solution(n, operand, operator_cnt):
     ans = [-10**9, 10**9]
     backtracking(operand[0], 1, operand, operator_cnt, ans)
     return ans

n = int(input())
operand = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
ans = solution(n, operand, operator_cnt)
print(int(ans[0]))
print(int(ans[1]))