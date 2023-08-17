# 크레인 인형뽑기 게임: 스택
def solution(board, moves):
    length = len(board)
    stack = []
    answer = 0
    for i in moves:
        for j in range(length):
            target = board[j][i-1]
            if target != 0:
                if stack and stack[-1] == target:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(target)
                board[j][i-1] = 0
                break
    return answer