def printSpace(times):
    for i in range(times):
        print("0", end="")

def printHashes(times):
    for i in range(times):
        print("#", end="")

def main():
    height = 24
    while height < 0 or height > 23:
        print("Height: ", end="")
        height = (int)(input())
    for line in range(height):
        printSpace(height - (line + 1))
        
        printHashes(line + 2)
        print("")
        
if __name__ == "__main__":
    main()





