import numpy as np

def wagonSpigot(digit):

    curPredigit = 0
    predigits = []
    
    # initialize array length 10n/3
    A = np.array([])
    for i in range(int( (digit * 10) / 3 )):
        A = np.append(A, 2)

    # core algorithm
    for n in range(digit):

        A = A * 10

        # put array A into regular form
        for i in range(digit, 1, -1):
            A[i-1] += (i-1)
            A[i] = A[i] % ((2 * i) - 1)

        curPredigit = A[0] // 10
        A[0] = A[0] % 10
        print(curPredigit)

wagonSpigot(10)
        


