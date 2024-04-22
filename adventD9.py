






def main():

    with open("adventOfCode/file.txt", 'r') as f:
        bigtotal = 0
        for line in f:
            lastPlace = []
            data = line.split()
            data = [int(i) for i in data]
            allZero = False
            while not allZero:
                allZero = True
                newData = []
                lastPlace.append(data[0])
                for i in range(len(data)-1):
                    diff = data[i+1]- data[i]
                    newData.append(diff)
                    if diff != 0:
                        allZero = False

                data = newData

            nextNum = 0
            for j in range(len(lastPlace)-1,-1,-1):
                nextNum = lastPlace[j] - nextNum

            bigtotal += nextNum

    print(bigtotal)




    
if __name__ == '__main__':
    main()
