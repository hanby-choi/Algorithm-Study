import os, random

def finishStudy(keywords, questions):
    print('<3번 이상 틀린 문제들>')
    for q, cnt in questions:
        if cnt >= 3:
            ans = keywords[q]
            sentence = ans + ": " + q 
            print(sentence)
    exit(0)

def getKeywords():
    root_path = 'C:\\Users\\Hanby\\Documents\\Github\\PythonStudy\\study\\keywords'
    folder_list = os.listdir(root_path)
    print('공부할 파일을 선택하세요.')
    for i, file in enumerate(folder_list):
        print(i+1, file)
    n = int(input())
    f = open('./keywords/' + folder_list[n-1], 'r', encoding='UTF-8')
    keywords = {}
    while True:
        new = f.readline().rstrip()
        if new == 'end':
            break
        word, meaning = new.split(': ')
        keywords[meaning] = word
    return keywords

def setQuestions(keywords):
    questions = [[m, 0] for m in keywords.keys()]
    return questions

def study(keywords, questions):
    n = len(questions)
    ans_index = set()
    wrong_index = set()
    print('공부를 시작합니다.')

    while True:
        rand_index = random.randint(0, n-1)
        if rand_index in ans_index:
            continue

        query = questions[rand_index][0] # 이번에 물어볼 키워드의 설명
        ans = keywords[query] # 이번에 물어볼 키워드 
        questions[rand_index][1] += 1 # 해당 키워드의 노출수 + 1
        
        print("(" + str(len(ans_index)) + "/" + str(n) + ") " + query + ": ")
        user_ans = input().rstrip()

        if user_ans == ans:
            ans_index.add(rand_index)
            wrong_index.discard(rand_index)
            print("맞았습니다!")
        elif user_ans == "end":
            print('<이번에 틀린 문제들>')
            for w in wrong_index:
                print(keywords[questions[w][0]] + ": " + questions[w][0])
            finishStudy(keywords, questions)
            print("프로그램을 종료합니다. 수고하셨습니다.")
        else:
            wrong_index.add(rand_index)
            print("틀렸습니다. 정답은 " + ans + "입니다.")

        if len(ans_index) == n:
            finishStudy(keywords, questions)
            print("모든 문제를 풀었습니다. 수고하셨습니다.")
        
keywords = getKeywords()
questions = setQuestions(keywords)
study(keywords, questions)