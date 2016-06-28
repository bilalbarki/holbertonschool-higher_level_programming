import time
from h_mul_matrix import MultiplicationMatrix

matrix_1 = ((1, 2, 3), (2, 3, 4), (3, 4, 5))
matrix_2 = ((0, 3, 1), (4, 1, 2), (1, 1, 2))

# matrix_1:
# 1  2  3
# 2  3  4
# 3  4  5

# matrix_2:
# 0  3  1
# 4  1  2
# 1  1  2

for i in [1, 2, 6, 10]:
    start = time.time()
    matrix_mul = MultiplicationMatrix(i, matrix_1, matrix_2)
    while matrix_mul.isComputing():
        pass
    print "With %d threads: %s in %f seconds" % (i, matrix_mul, (time.time() - start))
