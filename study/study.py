import os, random

root_path = 'C:\\Users\\Hanby\\Documents\\Github\\PythonStudy\\study\\keywords'
folder_list = os.listdir(root_path)
print('공부할 파일을 선택하세요.')
for i, file in enumerate(folder_list):
    print(i+1, file)
n = int(input())
f = open('./keywords/' + folder_list[n-1], 'r')

keywords = {}
while True:
    new = f.readline().rstrip()
    #print(new)
    if new == 'end':
        break
    word, meaning = new.split(': ')
    keywords[meaning] = word
meanings = list(keywords.keys())
n = len(meanings)
ans_index = set()
wrong_index = set()
print('공부를 시작합니다.')
while True:
    rand_index = random.randint(0, n-1)
    if rand_index in ans_index:
        continue

    query = meanings[rand_index]
    ans = keywords[query]
    
    print("(" + str(len(ans_index)) + "/" + str(n) + ") " + meanings[rand_index]+ ": ")
    user_ans = input().rstrip()

    if user_ans == ans:
        ans_index.add(rand_index)
        wrong_index.discard(rand_index)
        print("맞았습니다!")
    elif user_ans == "end":
        print('<이번에 틀린 문제들>')
        for w in wrong_index:
            print(keywords[meanings[rand_index]] + ": " + meanings[rand_index])
        print("프로그램을 종료합니다. 수고하셨습니다.")
        exit(0)
    else:
        wrong_index.add(rand_index)
        print("틀렸습니다. 정답은 " + ans + "입니다.")

    if len(ans_index) == n:
        print("모든 문제를 풀었습니다. 수고하셨습니다.")
        exit(0)
