
import socket
import threading

IP = '127.0.0.1'
PORT = 8008
MAX_COUNT = 4
HIT_PROB = 0.75


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
        while not self.done:
            (conn, addr) = self.server.accept()
            if len(self.clients) > MAX_COUNT:
                conn.send(b"ERROR_MAX_CONN")
                conn.close()
            else:
                conn.send(b"OK")
                self.clients.append(conn)
                t = threading.Thread(target=self.process, args=[conn])
                self.threads.append(t)
                t.start()

    def process(self, conn):
        pass

    def start(self):
        t = threading.Thread(target=self.accept)
        self.threads.append(t)
        t.start()
