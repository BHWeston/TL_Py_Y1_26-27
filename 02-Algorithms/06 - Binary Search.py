def binarySearch(toFind, items):
    iFirstIndex = 0
    iLastIndex = len(items) - 1
    while(iFirstIndex <= iLastIndex):
        iMidIndex = (iFirstIndex + iLastIndex) // 2

        if items[iMidIndex] == toFind:
            print("WOOOO IT EXISTS!!")
            return 0
        elif items[iMidIndex] < toFind:
            iFirstIndex = iMidIndex + 1
        else:
            iLastIndex = iMidIndex - 1


# Number that we want to find (this could be an input):
iNumberToFind = 5

# Create a list of numbers to find:
aArray = [1,3,4,5,6,8,11,15,16,18,19,21,29,35]

binarySearch(iNumberToFind, aArray)