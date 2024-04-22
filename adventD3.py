

def main():

    with open("adventOfCode/file.txt", 'r') as f:
        grid = []
        for line in f:
            grid.append(list(line.rstrip()))
    sum = 0
    for lineIndex in range(len(grid)):
        for element in range(len(grid[lineIndex])):
            if grid[lineIndex][element] == '*':
                
                starnums = checkStar(lineIndex, element, grid)
                if len(starnums) == 2:
                    sum += int(starnums[0]) * int(starnums[1])
    print(sum)

def checkStar(lineIndex, element, grid):

    starNums = []

    startIndex = element - 1
    endIndex = element + 1
    if element - 1 < 0:
        startIndex = 0
    elif element + 1 > len(grid[lineIndex]):
        endIndex = len(grid[lineIndex])
    start = -1
    end = 2
    if lineIndex == 0:
        start = 0
    elif lineIndex == len(grid)-1:
        end = 1
    for i in range(start, end):
        numbers = checkRow(lineIndex + i, grid, startIndex, endIndex, element)

        if len(numbers) == 2:
            return numbers
        elif len(numbers) == 1:
            starNums += numbers
    return starNums

def checkRow(lineIndex, grid, startIndex, stopIndex, element):
    
    numbers = []

    if not grid[lineIndex][element].isnumeric():
        nums = ''
        index = startIndex
        while(index >= 0 and grid[lineIndex][index].isnumeric()):
            nums = (grid[lineIndex][index]) + nums
            index -= 1
        if nums != '':
            numbers.append(nums)
        nums = ''
        index = stopIndex
        while(index < len(grid[lineIndex]) and grid[lineIndex][index].isnumeric()):
            nums = nums + (grid[lineIndex][index])
            index += 1
        if nums != '':
            numbers.append(nums)
        return numbers

    else:
        nums = grid[lineIndex][element]
        index = element - 1
        while(index >= 0 and grid[lineIndex][index].isnumeric()):
            nums = (grid[lineIndex][index]) + nums
            index -= 1
        index = element + 1
        while(index < len(grid[lineIndex]) and grid[lineIndex][index].isnumeric()):
            nums = nums + (grid[lineIndex][index])
            index += 1
        numbers.append(nums)
        return numbers

if __name__ == '__main__':
    main()



