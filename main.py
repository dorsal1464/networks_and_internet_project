
import server
import client
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # q = [{'title': 'title', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 'correct': 3}]
    # json.dump(q, open('questions.json', 'r+'))
    text, corr = server.query_question()
    print(text, "correct:", corr)
    if input("choose s or c (client or server): ") == 's':
        o = server.Server()
        print("server")
    else:
        o = client.Client()
        print("client")
    o.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
