
def main():
    
    futureCard = [0,0,0,0,0,0,0,0,0,0]

    with open("adventOfCode/file.txt", 'r') as f:
        matchesSum = 0
        for line in f:
            cardMatches = 0
            line.rstrip()
            carddata = line.split(':')[1]
            cardWinAndNums = carddata.split('|')
            cardWinNums = cardWinAndNums[0].split()
            cardNums = cardWinAndNums[1].split()
            
            for winNum in cardWinNums:
                if winNum in cardNums:
                    cardMatches += 1
            
            cards = futureCard.pop(0) + 1
            futureCard.append(0)
            matchesSum += cardMatches * cards + 1
            for i in range(cardMatches):
                futureCard[i] += 1 * cards
            
        print(matchesSum)
            

if __name__ == '__main__':
    main()
