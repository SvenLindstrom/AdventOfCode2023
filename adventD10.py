
def main():
    testDic = {'F':1,'L':-1,'J':1,'7':-1}
    with open("adventOfCode/file.txt", 'r') as f:
        pipeMap = []
        positions = []
        totalVol = 0
        stepCount = 0
        for line in f:
            if 'S' in line:
                positions.append(len(pipeMap))
                positions.append(line.find('S'))
            pipeMap.append(line.rstrip())
        cordDic = {}
        #cordDic[positions[0]] = [positions[1]]
        positions[1] += 1
        cordDic[positions[0]] = [positions[1]]
        change = []
        change.append(0)
        change.append(1)
        while pipeMap[positions[0]][positions[1]] != 'S':
            stepCount += 1
            #print(positions)
            #print(pipeMap[positions[0]][positions[1]])
            match pipeMap[positions[0]][positions[1]]:
                case '|' | '-':
                    positions[bool(change[1])] += change[bool(change[1])]
                case 'L'| '7':
                    positions[bool(change[0])] += change[not change[0]]
                    temp = change[0]
                    change[not temp], change[temp] = 0, change[not temp]
                case 'J' | 'F':
                    positions[bool(change[0])] += change[not change[0]] * -1
                    temp = bool(change[0])
                    change[not temp], change[temp] = 0, change[not temp] * -1                               
            

            if pipeMap[positions[0]][positions[1]] in '|7LFJ':
                if positions[0] in cordDic: 
                    val = cordDic.get(positions[0]) + [positions[1]]
                    
                    cordDic[positions[0]] = val
                else:
                    cordDic[positions[0]] = [positions[1]]
                
        
        for key in cordDic.keys():

            nums = cordDic[key]
            nums = sorted(nums)

            inLoop = False
            onEdge = False
            subString = pipeMap[key][nums[0]:nums[-1]+1]
            tracker = 0
            for i in range(len(subString)):
                letter = pipeMap[key][i + nums[0]]
                if letter == 'S':
                    letter = '-'
                if i + nums[0] in nums:
                    if letter == '|':
                        inLoop = not inLoop

                    elif letter in 'LF':
                        tracker += testDic[letter]
                        onEdge = True
                    else:
                        tracker += testDic[letter]
                        onEdge = False
                        if tracker:
                            inLoop = not inLoop
                        tracker = 0

                elif inLoop and not onEdge:
                    totalVol += 1

                        

    for key in cordDic.keys():
        print(cordDic[key])
    print(totalVol)
                







if __name__ == '__main__':
    main()