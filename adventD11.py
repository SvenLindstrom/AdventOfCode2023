
import time


def main():
    map = []
    totalDistance = 0
    xMillionCord = []
    yMillionCord = []
    
    with open("adventOfCode/file.txt", 'r') as f:
        cordList = []
        for line in f:
            line = line.rstrip()     
            line = [i for i in line]
            if line.count('#') == 0:
                yMillionCord.append(len(map)-1)
            else:
                for i in range(len(line)):
                    if line[i] == '#':
                        cordList.append([len(map),i])
            map.append(line)
        i = 0
        while i < len(map[0]):
            hasTag = False
            for row in map:
                if row[i] == '#':
                    hasTag = True
                    break
            if not hasTag:
                xMillionCord.append(i)
            i += 1

        # for l in map:
        #     print(l)
        start =time.time()
        for i in range(len(cordList)-1):
            g1 = cordList[i]
            for j in range(i+1,len(cordList),1):
                g2 = cordList[j]
                yChange = g2[0] - g1[0]
                yFinalChange = yChange
                
                for y in yMillionCord:
                    if y < g1[0]:
                        yMillionCord.remove(y)
                        continue
                    elif y > g1[0] + yChange:
                        break
                    if y in range(g1[0],g1[0] + yChange):
                        yFinalChange += 999999

                xChange = g2[1]-g1[1]
                xFinalChange = abs(xChange)
                for x in xMillionCord:
                    step = 1
                    if xChange < 0:
                        step = -1  
                    if x in range(g1[1],g1[1]+xChange,step):
                        xFinalChange += 999999
                dist = yFinalChange + xFinalChange

                # print(g1)
                # print(g2)
                # print(dist)
                totalDistance += dist
        end = time.time()
        print(f'time to calc: {end - start}')
    
    # print(xMillionCord)
    # print(yMillionCord)

    # print(cordList)
    print(totalDistance)


if __name__ == '__main__':

    main()
