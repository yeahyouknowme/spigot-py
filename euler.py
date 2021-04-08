import numpy as np


def saleSpigot(digit):
    
    # initialize array
    spigotArray = np.array([])
    for x in range(digit+1):
        spigotArray = np.append(spigotArray, 1)

    # print digits of euler's number 
    for n in range(digit):

        spigotArray = spigotArray * 10

        # LOOP THROUGH ARRAY BACKWARDS #
        # divide each item by its position + 2
        # add quotient to next item
        # set cur item to remainder
        for i in range(digit, 0, -1):
            ans = divmod(spigotArray[i], (i+2))
            spigotArray[i] = int(ans[1])
            spigotArray[i-1] += int(ans[0])
        
        # drip[0] is the nth digit of euler's number
        drip = divmod(spigotArray[0], 2)
        spigotArray[0] = int(drip[1])
        print(drip[0])


        

saleSpigot(10)



