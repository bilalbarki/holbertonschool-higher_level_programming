import threading
'''reverses string but with right order'''
class ReverseStrThread(threading.Thread):
    sentence = ""
    lock = threading.Lock()
    def __init__(self, word):
        threading.Thread.__init__(self)
        if not isinstance(word, str):
            raise Exception("word is not a string")
        self.__word = word

    def run(self):
        ReverseStrThread.lock.acquire()
        ReverseStrThread.sentence += self.__word[::-1] + " "
        ReverseStrThread.lock.release()
