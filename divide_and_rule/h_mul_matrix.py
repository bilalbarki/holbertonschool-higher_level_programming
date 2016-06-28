import threading
'''multiplies a square matrix with multithreading'''
class MultiplicationMatrix():
    mult = []
    def __init__(self, nb_threads, matrix_1, matrix_2):
        if not isinstance(nb_threads, int):
            raise Exception("nb_threads is not an integer")
        for i in range (len(matrix_1)):
            if len(matrix_1) != len(matrix_1[i]):
                raise Exception("matrix_1 is not a square matrix")

        for i in range (len(matrix_2)):
            if len(matrix_2) != len(matrix_2[i]):
                raise Exception("matrix_2 is not a square matrix")

        if len(matrix_1) != len(matrix_2):
            raise Exception("matrix_1 and matrix_2 don't have the same size")
        w = len(matrix_1)
        MultiplicationMatrix.mult = [[0 for x in range(w)] for y in range(w)] 
        self.__threads = []
        k=0
        for x in range(len(matrix_1)):
            for y in range(len(matrix_2)):
                k+=1
                thread = MultiplicationMatrixThread(x , y, matrix_1[x], [row[y] for row in matrix_2])
                self.__threads += [thread]
                thread.start()
                if (k == nb_threads):
                    while self.isComputing():
                        pass
                    k=0
    
    '''checks if all threads have completed their work'''
    def isComputing(self):
        for thread in self.__threads:
            if thread.isAlive():
                return True
        return False

    '''for printing'''
    def __str__(self):
        hello = tuple(map(tuple, MultiplicationMatrix.mult))
        return str(hello)

class MultiplicationMatrixThread(threading.Thread):
    lock = threading.Lock()
    def __init__(self, x, y, row_matrix_1, column_matrix_2):
        threading.Thread.__init__(self)
        if not isinstance(x, int):
            raise Exception("x or y is not a integer")
        if not isinstance(y, int):
            raise Exception("x or y is not a integer")
        for num in row_matrix_1:
            if not isinstance(num, int):
                Exception("row_matrix_1 is not an array of integers")
        for num in column_matrix_2:
            if not isinstance(num, int):
                Exception("row_matrix_2 is not an array of integers")
        self.x = x
        self.y = y
        self.row_matrix_1 = row_matrix_1
        self.column_matrix_2 = column_matrix_2

    def run(self):
        temp = 0
        for i in range(len(self.row_matrix_1)):
            temp += self.row_matrix_1[i] * self.column_matrix_2[i]
        self.lock.acquire()
        MultiplicationMatrix.mult[self.x][self.y] = temp
        self.lock.release()
        
