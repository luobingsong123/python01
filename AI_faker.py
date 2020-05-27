while(True):
    question = input()
    answer = question.replace('吗', '呢',2)
    answer = answer.replace('你', '我')
    answer = answer.replace('？', '！')
    print(answer)