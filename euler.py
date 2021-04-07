import numpy as np


## FINAL RESULT IS SOMETIMES WRONG ???? ##
def spigot(digit):
    
    # initialize array
    spigotArray = np.array([])
    for x in range(digit):
        spigotArray = np.append(spigotArray, int(1))
    
    for n in range(0, digit, 1):
        ## SINGLE STEP THROUGH ALGHORITHM ##
        spigotArray = spigotArray * 10
        # loop through array #
        for i in range(digit-1, 0, -1):
            ans = divmod(spigotArray[i], (i+2))

            spigotArray[i] = int(ans[1])
            spigotArray[i-1] += int(ans[0])
        drip = int(spigotArray[0]) // 2
        spigotArray[0] = spigotArray[0] % 2
        print(drip)


        

spigot(10)



