import threading
import urllib

class LoripsumThread(threading.Thread):
    lock = threading.Lock()
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.__filename = filename

    def run(self):
        req = urllib.urlopen('http://loripsum.net/api/1/short')
        #open(self.__filename, 'w').close()
        LoripsumThread.lock.acquire()
        with open(self.__filename, "a") as text_file:
            text_file.write(req.read())
        LoripsumThread.lock.release()
