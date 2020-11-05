
import socket
import threading
import json
import random

IP = '127.0.0.1'
PORT = 8008
MAX_COUNT = 4
HIT_PROB = 0.75


def query_question():
    # question format:
    # { 'title':
    #   1:
    #   2:
    #   3:
    #   4:
    #   'correct':
    # }
    questions = json.load(open('questions.json', 'r'))
    q = random.choice(questions)
    # create random permutation
    lst = ['1', '2', '3', '4']
    perm = list()
    for i in range(0, 4):
        a = random.choice(lst)
        lst.remove(a)
        perm.append(a)
    print(perm)
    new_correct = perm.index(q['correct']) + 1
    text = "{}:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(q['title'], q[perm[0]], q[perm[1]], q[perm[2]], q[perm[3]])
    return text, new_correct


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = list()
        self.threads = list()
        self.done = False
        self.ip = IP
        self.port = PORT
        self.server.bind((IP, PORT))
        self.server.listen(5)

    def accept(self):
        # accept new connections
        while not self.done:
            (conn, addr) = self.server.accept()
            if len(self.clients) > MAX_COUNT:
                # max conn achieved...
                conn.send(b"ERROR_MAX_CONN")
                conn.close()
            else:
                # validate and and to client list
                conn.send(b"OK")
                self.clients.append(conn)
                # start processing client
                t = threading.Thread(target=self.process, args=[conn])
                self.threads.append(t)
                t.start()

    def process(self, conn):
        pass

    def start(self):
        # start the server
        self.accept()
