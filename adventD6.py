#from memory_profiler import profile
import time as timer
import math

#@profile
def main():
    start = timer.time()
    with open("adventOfCode/file.txt", 'r') as f:
        times = f.readline().split(":")[1].split()
        temp = ''
        for time in times:
            temp += time
        times = int(temp)
        distance = f.readline().split(":")[1].split()
        temp = ''
        for dist in distance:
            temp += dist
        distance = int(temp)

        possibleW = 0
        for j in range(times):
            if distance < (j * ((times-j))):
                if possibleW == 0:
                    possibleW += ((times-j)) - j +1
                break
        print(possibleW)
    end = timer.time()
    print(f"it took: {end - start}")


@profile
def test():
    start = timer.time()
    with open("adventOfCode/file.txt", 'r') as f:
        times = int(f.readline().split(":")[1].replace(" ",""))
        distance = int(f.readline().split(":")[1].replace(" ",""))
        c = math.ceil(((-1*times)+ math.sqrt((times * times) - 4 * (-1)*(distance * -1)))/(-2))
        print(((times-c)) - c +1)
    end = timer.time()
    print(f"it took: {end - start}")



if __name__ == '__main__':
    test()