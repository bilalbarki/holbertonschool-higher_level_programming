import threading
'''produces fibonacci numbers with multithreading support'''
class FibonacciThread(threading.Thread):
    lock = threading.Lock()
    def __init__(self, number):
        threading.Thread.__init__(self)
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        self.__number = number

    def run(self):
        n1=0
        n2=1
        for i in range(self.__number):
            temp=n1
            n1=n2
            n2=temp+n1
        self.lock.acquire()
        print "%d => %d" % (self.__number, n1)
        self.lock.release()

