
import socket
from levels import *

IP = '127.0.0.1'
PORT = 8008


class Client:
    def __init__(self):
        # connect to server...
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        print("Welcome to HaMirdaf!")
        print("Would you like to play?")
        if input(">>> ") not in ["yes", "Yes"]:
            return
        try:
            self.conn.connect((IP, PORT))
        except socket.SO_ERROR:
            print("server offine")
            return
        # connection successful...
        msg = self.conn.recv(256)
        if msg == b"OK":
            self.converse()
        elif msg == b"ERROR_MAX_CONN":
            # server is full...
            print("server is full, retry later...")
            self.conn.close()
        else:
            # unidentified protocol
            print("unidentified server, disconnecting...")
            self.conn.close()

    def converse(self):
        print("Level 1:")
        client_level_1(self.conn)
