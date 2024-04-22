
#from memory_profiler import profile
import time

#@profile
def main():
    starttime = time.time()
    finalSeed = []
    with open("file.txt", 'r') as f:
        seedsRanges = f.readline().rstrip().split(":")[1].split()
        seedsRanges = [int(i) for i in seedsRanges]

    for i in range(0,len(seedsRanges),2):
        with open("file.txt", 'r') as f:
            #print('making memes')
            ranges = []
        
            ranges.append([seedsRanges[i], seedsRanges[i+1]])
    
            mapings = []
            f.readline()
            f.readline()
            f.readline()
            #print('about to start reading')
            for line in f:
                if line == "\n":
                    f.readline()
                    
                    
                    mapStart = {}
                    for map in mapings:
                        mapStart[map[1]] = map
                    start = sorted(mapStart.keys())

                    mapings = []
                    newRanges = []
                    #print('eval')
                    #print(ranges)
                    for rang in ranges:
                        rangeUpper = rang[0]+rang[1] - 1
                        rangeLower = rang[0]
                        for i in start:
                            map = mapStart[i]
                            mapUpper = map[1]+map[2] - 1
                            mapLower = map[1]
                            if (rangeUpper < mapLower) or (mapUpper < rangeLower):
                                continue
                            elif mapLower < rangeLower and mapUpper > rangeUpper:
                                newRanges.append([map[0]+(rangeLower - mapLower), rangeUpper - rangeLower+1])
                                rangeLower = rangeUpper + 1
                                break
                            elif mapLower <= rangeLower and (mapUpper >= rangeLower and mapUpper <= rangeUpper):
                                newRanges.append([map[0]+(rangeLower - mapLower), mapUpper - rangeLower+1])
                                rangeLower = mapUpper + 1

                            elif mapLower > rangeLower and mapUpper < rangeUpper:
                                newRanges.append([rangeLower, mapLower-rangeLower])
                                newRanges.append([map[0], map[2]])
                                rangeLower = mapUpper + 1

                            elif (mapLower <= rangeUpper and mapLower >= rangeLower) and mapUpper >= rangeUpper:
                                newRanges.append([map[0],  rangeUpper - mapLower+1])
                                rangeLower = rangeUpper + 1
                                break

                        if rangeLower < rangeUpper:
                            newRanges.append([rangeLower, rangeUpper - rangeLower+1])
                         
                    if newRanges:
                        ranges = newRanges
                    #print('eval finished')
                    continue

                nums = line.split()
                nums = [int(i)for i in nums]
                mapings.append(nums)
            

            mapStart = {}
            for map in mapings:
                mapStart[map[1]] = map
            start = sorted(mapStart.keys())

            mapings = []
            newRanges = []
            #print('eval')
            #print(ranges)
            for rang in ranges:
                rangeUpper = rang[0]+rang[1] - 1
                rangeLower = rang[0]
                for i in start:
                    map = mapStart[i]
                    mapUpper = map[1]+map[2] - 1
                    mapLower = map[1]
                    if (rangeUpper < mapLower) or (mapUpper < rangeLower):
                        continue
                    elif mapLower < rangeLower and mapUpper > rangeUpper:
                        newRanges.append([map[0]+(rangeLower - mapLower), rangeUpper - rangeLower+1])
                        rangeLower = rangeUpper + 1
                        break
                    elif mapLower <= rangeLower and (mapUpper >= rangeLower and mapUpper <= rangeUpper):
                        newRanges.append([map[0]+(rangeLower - mapLower), mapUpper - rangeLower+1])
                        rangeLower = mapUpper + 1

                    elif mapLower > rangeLower and mapUpper < rangeUpper:
                        newRanges.append([rangeLower, mapLower-rangeLower])
                        newRanges.append([map[0], map[2]])
                        rangeLower = mapUpper + 1

                    elif (mapLower <= rangeUpper and mapLower >= rangeLower) and mapUpper >= rangeUpper:
                        newRanges.append([map[0],  rangeUpper - mapLower+1])
                        rangeUpper = mapLower - 1
                        break

                if rangeLower < rangeUpper:
                    newRanges.append([rangeLower, rangeUpper - rangeLower+1])
                    
            if newRanges:
                ranges = newRanges
            #print('eval finished')
            

        smallest = []
        for rang in ranges:
            smallest.append(rang[0]) 
        finalSeed.append(min(smallest))
    print(min(finalSeed))
    end = time.time()
    print(f"it took: {end - starttime}")

if __name__ == '__main__':
    main()





                    # mapIndex = 0
                    # seedCopy = []
                    # for i in seeds:
                    #         while mapStart[start[mapIndex]][1]+mapStart[start[mapIndex]][2] <= i and mapIndex < len(start)-1:
                    #                 mapIndex += 1
                    #         if mapStart[start[mapIndex]][1] <= i < (mapStart[start[mapIndex]][1]+mapStart[start[mapIndex]][2]):
                    #             seedCopy.append(i - mapStart[start[mapIndex]][1] + mapStart[start[mapIndex]][0])
                    #         else:
                    #             seedCopy.append(i)
                    # seedCopy.sort() 
                    # seeds =  seedCopys
