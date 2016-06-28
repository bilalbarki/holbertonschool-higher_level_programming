import threading, sys
'''string length with multithreading support'''
class StrLenThread(threading.Thread):
    def __init__(self, word):
        threading.Thread.__init__(self)
        if not isinstance(word, str):
            raise Exception("word is not a string")
        self.__word = word
        
    def run(self):
        global total_str_length
        total_str_length += len(self.__word)

#main
str_length_threads = []
words = sys.argv[1].split(" ")
total_str_length = len(words) - 1
str_length_threads = []
for word in words:
    str_length_thread = StrLenThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()
    
print "%d" % total_str_length
