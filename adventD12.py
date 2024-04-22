
global counter 

def main():
    global counter
    counter = 0
    with open("adventOfCode/file.txt", 'r') as f:
        for line in f:
            splitData = line.rstrip().split()
            springs = splitData[0].split('.')
            springs = [i for i in springs if i!='']
    
            arrangement = splitData[1].split(',')
            arrangement  = [int(i) for i in arrangement]

            print(springs)
            print(arrangement)

            # littleSum = 0
            # if len(springs) == len(arrangement):
            #     for i in range(len(springs)):
            #         if len(springs[i]) != arrangement[i]:
            #             hashCount = springs[i].count('#')
            #             littleSum += ((len(springs[i])-hashCount) - (arrangement[i]-hashCount)) + 1


            #     if littleSum == 0:
            #         littleSum += 1
            #     counter += littleSum

            # else:
            newSpings = ''
            for spring in springs:
                # if spring.count('#') == len(spring):
                #     arrangement.remove(len(spring))
                # else:  
                    newSpings += spring +'.'
            
            
            global arrangemen
            arrangemen = arrangement
            valFormat(newSpings, 0)
            print(counter)
        print(counter)

                        
def valFormat(newSpings, arrangIndex):
    global counter
    if  arrangIndex > len(arrangemen)-1 or len(newSpings) - 1 < arrangemen[arrangIndex]:
        return
    for j in range(len(newSpings)):
        maekit = True
        for i in range(arrangemen[arrangIndex]):
            if newSpings[i+j] == '.':
                maekit = False
                break
        if maekit and newSpings[i+j+1] != '#':
            if arrangIndex == len(arrangemen)-1 and '#' not in newSpings[i+j+1:]:
                counter += 1
            if newSpings[j] == '#':
                newSping = newSpings[j+arrangemen[arrangIndex]+1:]
                valFormat(newSping, arrangIndex+1)
                return
            else:
                newSping = newSpings[j+arrangemen[arrangIndex]+1:]
                valFormat(newSping, arrangIndex+1)
        elif len(newSpings) - 2 < arrangemen[arrangIndex]+j or newSpings[j] == '#':
            return
    return
    

if __name__ == '__main__':
    main()
