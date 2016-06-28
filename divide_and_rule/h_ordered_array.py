import threading
'''basic sorting with multithreading, very slow though'''
class OrderedArray():
    list = []

    def __init__(self):
        self.__threads = []

    def add(self, number):
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        thread = OrderedArrayThread(number)
        self.__threads += [thread]
        thread.start()

    def isSorting(self):
        for thread in self.__threads:
            if thread.isAlive():
                return True
        return False

    def __str__(self):
        return str(OrderedArray.list)


class OrderedArrayThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        self.__number = number

    def run(self):
        OrderedArrayThread.lock.acquire()
        OrderedArray.list.append(self.__number)
        OrderedArray.list.sort()
        OrderedArrayThread.lock.release()
