
import time
import math
from memory_profiler import profile

#@profile
def main():

    with open("adventOfCode/file.txt", 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        stepMap = {}

        currentNodes = []
        for line in f:
            lineSplit = line.split('=')
            node = lineSplit[0].rstrip()
            leftRight = lineSplit[1].strip().lstrip('(').rstrip(')').split(', ')
            stepMap[node] = leftRight
            if node[2] == 'A':
                currentNodes.append(node)
                
        stepCount = 0
        notAllZZZ = True 
        stepcounts = []
        start = time.time()
        while notAllZZZ:
            #print(stepCount)
            direction = instructions[stepCount % len(instructions)]
            notAllZZZ = False
            for i in range(len(currentNodes)):
                if currentNodes[i] is not None:
                    currentNodes[i] = stepMap[currentNodes[i]][direction == 'R']
                    if currentNodes[i][2] != 'Z':
                        notAllZZZ = True
                    else:
                        stepcounts.append(stepCount+1)
                        currentNodes[i] = None
            stepCount += 1
        end = time.time()
        print(f'Find step time: { end - start}')
        
        totalStep = 1
        start = time.time()
        for count in stepcounts:
            totalStep = math.lcm(totalStep, count)
        end = time.time()
        print(f'LCM time: { end - start}')

        print(totalStep)



if __name__ == '__main__':
    main()
