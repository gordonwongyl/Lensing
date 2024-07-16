import os
import numpy as np
# POSX = list(np.linspace(0.3, 0.4, 11))
# POSY = list(np.linspace(0.5, 0.6, 11))
POSX = [0.373]
POSY = [0.550]
MASS = [str(i) + 'e' + str(j) for i in range(1, 10, 1) for j in range(12, 15)]
RESULT = []

def explore():
    for x in POSX:
        for y in POSY:
            for m in MASS:
                resultfile = open("result.txt", "w+")
                file = open("point.input", "r")
                text = file.readlines()
                file.close()
                line = text[29].split()
                line[5] = str(y)
                line[4] = str(x)
                line[3] = m
                line = " ".join(line)
                text[29] = line + '\n'
                file = open("point.input", 'w')
                file.writelines(text)
                file.close()
                os.system("glafic point.input")
                output = open("out_optresult.dat")
                chisq = output.readlines()[-11].split()[2]
                x = str(x)
                y = str(y)
                res = " ".join([x,y,m,chisq])
                print(res)
                RESULT.append(res)
                resultfile.writelines([res+'\n'])
                resultfile.close()
                output.close()

explore()
os.system('clear')
print(RESULT)