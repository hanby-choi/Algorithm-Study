# 이진 검색 트리: 그래프, 트리, 재귀
def postOrder(left, right, tree, result):
    if left > right:
        return
    root = tree[left]
    temp = left+1
    for i in range(left+1, right+1):
        if tree[i] > root:
            temp = i
            break
    postOrder(left+1, temp-1, tree, result)
    postOrder(temp, right, tree, result)
    result.append(root)
    
def solution(tree):
    result = []
    postOrder(0, len(tree)-1, tree, result)