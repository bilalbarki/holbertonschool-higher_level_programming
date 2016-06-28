import threading
'''calculates sum using multithreading'''
class Sum():
    sum = 0
    def __init__(self, nb_threads, numbers):
        if not isinstance(nb_threads, int):
            raise Exception("nb_threads is not an integer")
        if not isinstance(numbers, list):
            raise Exception("numbers is not an array of integers")
        self.__threads = []
        self.__nb_threads = nb_threads
        Sum.sum = 0
        if len(numbers) >= nb_threads:
            nSlices = nb_threads
        else:
            nSlices = len(numbers)
        slices = [len(numbers) // (nSlices)] * nSlices
        remainder = len(numbers)-sum(slices)
        slices[:remainder] = [i + 1 for i in slices[:remainder]]
        splittedList = [numbers[sum(slices[:ii]):sum(slices[:ii+1])] for ii in range(nSlices)]
        for splitt in splittedList:
            thread = SumThread(splitt)
            self.__threads += [thread]
            thread.start()
    '''checks if all threads have finished their tasks'''            
    def isComputing(self):
        for thread in self.__threads:
            if thread.isAlive():
                return True
        return False
    '''for printing'''
    def __str__(self):
        return str(Sum.sum)
        

class SumThread(threading.Thread):
    lock = threading.Lock()
    def __init__(self, numbers):
        threading.Thread.__init__(self)
        if not isinstance(numbers, list):
            raise Exception("numbers is not an array of integers")
        self.__numbers = numbers

    def run(self):
        temp = 0
        for number in self.__numbers:
            temp += number
        SumThread.lock.acquire()
        Sum.sum += temp
        SumThread.lock.release()
