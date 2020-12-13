import json
import random
import time
DELAY = 3

def get_questions():
    questions = json.load(open('questions.json', 'r'))
    return questions


def query_question(questions):
    # question format:
    # { 'title':
    #   1:
    #   2:
    #   3:
    #   4:
    #   'correct':
    # }
    q = random.choice(questions)
    questions.remove(q)
    # create random permutation
    lst = ['1', '2', '3', '4']
    perm = list()
    for i in range(0, 4):
        a = random.choice(lst)
        lst.remove(a)
        perm.append(a)
    print(perm)
    # select and format
    new_correct = perm.index(q['correct']) + 1
    text = "{}:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(q['title'], q[perm[0]], q[perm[1]], q[perm[2]], q[perm[3]])
    return text, new_correct


def client_level_1(sock):
    print("You will be presented with 3 questions, and you have to choose one of the answers (1 to 4)")
    for i in range(0,3):
        # repeat 3 times
        print("Question: "+str(i+1))
        print(sock.recv(1024).decode('utf-8'))
        sock.send(input(">>> ").encode('utf-8'))
        print(sock.recv(1024).decode('utf-8'))
        time.sleep(DELAY)
    print(sock.recv(1024).decode('utf-8'))


def server_level_1(sock):
    score = 0
    questions = get_questions()
    for i in range(0,3):
        # repeat q 3 times...
        text, correct = query_question(questions)
        sock.send(text.encode('utf-8'))
        msg = sock.recv(1024).decode('utf-8')
        try:
            if int(msg) == correct:
                score += 1
                sock.send(b"Correct!")
            else:
                sock.send(b"Wrong!")
        except Exception as e:
            sock.send(b"Invalid option, Wrong answer!")
    return score
