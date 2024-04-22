
from memory_profiler import profile
import time 

cardValMap = {'A':14,'K':13,'Q':12,'J':1,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

@profile
def main(doing_merge):
    with open("adventOfCode/file.txt", 'r') as f:
        handBidMap = {}
        handsStrengthListList = [[] for _ in range(7)]
        for line in f:
            lineData = line.split()
            handBidMap[lineData[0]] = int(lineData[1])
            freq = {}
            joke = False
            for c in lineData[0]:
                freq[c] = freq.get(c,0) + 1

            frqKey = list(freq.keys())
            if doing_merge:
                putList(freq, frqKey, handsStrengthListList, lineData)
            else:
               insetion(freq, frqKey, handsStrengthListList, lineData) 

        return handsStrengthListList, handBidMap

def putList(freq, frqKey, handsStrengthListList, lineData):
    match len(frqKey):
        case 1 | 0:
            handsStrengthListList[6].append(lineData[0])
        case 2:
            if freq[frqKey[0]] == 1 or freq[frqKey[1]] == 1:
                handsStrengthListList[5].append(lineData[0])
            else:
                handsStrengthListList[4].append(lineData[0])   
        case 3:
            if (freq[frqKey[0]] != 2 and freq[frqKey[1]] !=2) or "J" in lineData:
                handsStrengthListList[3].append(lineData[0])
            else:
                handsStrengthListList[2].append(lineData[0])
        case 4:
            handsStrengthListList[1].append(lineData[0])
        case 5:
            handsStrengthListList[0].append(lineData[0])



def insetion(freq, frqKey, handsStrengthListList, lineData):
    match len(frqKey):
        case 1 | 0:
            insertHand(handsStrengthListList[6], lineData[0])
        case 2:
            if freq[frqKey[0]] == 1 or freq[frqKey[1]] == 1:
                insertHand(handsStrengthListList[5], lineData[0])
            else:
                insertHand(handsStrengthListList[4], lineData[0])
        case 3:
            if (freq[frqKey[0]] != 2 and freq[frqKey[1]] !=2) or 'J' in lineData:
                insertHand(handsStrengthListList[3], lineData[0])
            else:
                insertHand(handsStrengthListList[2], lineData[0])
        case 4:
            insertHand(handsStrengthListList[1], lineData[0])
        case 5:
            insertHand(handsStrengthListList[0], lineData[0])

def merge(list):
    if len(list) == 1:
        return list
    list1 = merge(list[:((len(list)//2)):])
    list2 = merge(list[(len(list)//2)::])

    i = 0
    j = 0
    newList = []
    while(i < len(list1) and j < len(list2)):
        if handEqual(list1[i], list2[j]):
            newList.append(list2[j])
            j += 1
        else:
            newList.append(list1[i])
            i += 1
    
    if i < len(list1):
        newList += list1[i:]
    elif j < len(list2):
        newList += list2[j:]

    return newList

def insertHand(Handlist, hand):
    start = 0
    end = len(Handlist)-1
    mid = (end + start) // 2
    if len(Handlist) == 0:
        Handlist.append(hand)
        return
    while start <= end:
        mid = (end + start) // 2
        if mid == len(Handlist)-1:
            if handEqual(Handlist[mid], hand) == 0:
                Handlist.append(hand)
                return
            else:
                end = mid - 1
        
        elif mid == 0:
            if handEqual(Handlist[mid], hand) == 1:
                Handlist.insert(mid, hand)
                return
            elif handEqual(Handlist[mid], hand) == 0 and handEqual(Handlist[mid+1], hand) == 1: 
                Handlist.insert(mid+1, hand)
                return
            else:
                start = mid +1
                
        elif handEqual(Handlist[mid],hand) == 0 and handEqual(Handlist[mid+1],hand) == 0:
            start = mid +1
        elif  handEqual(Handlist[mid],hand) == 1 and handEqual(Handlist[mid+1],hand) == 1:
            end = mid -1
            
        else:
            Handlist.insert(mid+1, hand)
            return
    Handlist.insert(mid, hand)



def handEqual(hand1, hand2):
    for i in range(len(hand1)):
        if cardValMap[hand1[i]] < cardValMap[hand2[i]]:
            return 0
        elif cardValMap[hand1[i]] > cardValMap[hand2[i]]:
            return 1



def binaryInsertSolution():
        handsStrengthListList, handBidMap = main(False)
        totalBid = 0
        position = 1
        for cardSet in handsStrengthListList:
            for card in cardSet:
                totalBid += handBidMap[card] * position
                position += 1

        print(totalBid)
   
def merg_solution():
    data, handBidMap = main(True)
    postionCount = 1
    bigSum = 0
    start = time.time()
    for date in data:
        date = merge(date)
        for dat in date:
            bigSum += handBidMap[dat] * postionCount
            postionCount += 1
    end = time.time()
    print(f'it took: {end - start}')
    print(bigSum)


if __name__ == '__main__':
    start = time.time()
    merg_solution()
    end = time.time()
    print(f'it took: {end - start}')