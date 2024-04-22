
def main():


    with open("adventOfCode/file.txt", 'r') as f:
        total = 0
        for line in f:
            
            line = line.strip()
            for letter in line:
                if letter.isnumeric():
                    first = letter
                    break
            for i in range(len(line)-1,-1,-1):
                if line[i].isnumeric():
                    second = line[i]
                    break
            num = first + second
            total += int(num)
    
    print(total)
if __name__ == '__main__':
    main()