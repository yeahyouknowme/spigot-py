import numpy as np


def spigot(digit):
    
    # initialize array
    spigotArray = np.array([])
    for x in range(digit+1):
        spigotArray = np.append(spigotArray, int(1))

    # print digits of euler's number 
    for n in range(0, digit, 1):

        spigotArray = spigotArray * 10

        # LOOP THROUGH ARRAY BACKWARDS #
        # divide each item by its position + 2
        # add quotient to next item
        # set cur item to remainder
        for i in range(digit, 0, -1):
            ans = divmod(spigotArray[i], (i+2))
            spigotArray[i] = int(ans[1])
            spigotArray[i-1] += int(ans[0])
        drip = int(spigotArray[0]) // 2
        spigotArray[0] = spigotArray[0] % 2
        print(drip)


        

spigot(10)



