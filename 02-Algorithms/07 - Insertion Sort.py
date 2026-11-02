def insertionSort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition -1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition -1

        array[currentPosition] = currentValue
    return array

userArray = [10, 1, 5, 64, 12, 35, 44]
sortedArray = insertionSort(userArray)
print(sortedArray)