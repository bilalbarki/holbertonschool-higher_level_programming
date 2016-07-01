import threading
from random import randint
from time import sleep

class Store():
    def __init__(self, item_number, person_capacity):
        self.__item_number = item_number
        self.__pool = threading.Semaphore(value = person_capacity)
        #self.__nbpersoninside = 0

    def enter(self):
        self.__pool.acquire()
        #self.__nbpersoninside += 1

    def buy(self):
        sleep(randint(5,10))
        bought = False
        if self.__item_number > 0:
            self.__item_number -= 1
            bought = True
        #self.__nbpersoninside -= 1
        self.__pool.release()
        return bought
