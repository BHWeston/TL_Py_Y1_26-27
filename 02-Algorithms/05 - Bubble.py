# Bubble Sort Algorithm:

# Create an unsorted list of numbers:
lUnsortedList = [5,1,6,8,9,7,4,3,2,4] 

# Get the length of the array:
iLengthList = len(lUnsortedList)

# Get the length and -1 off this:
iIndexLength = iLengthList - 1

# Making a while to go through the length of our array, so long as it is greater than 1:
while iLengthList > 1:

    # Inside the while, we are going to have a for that goes through each of the items in the list:
    for i in range(0, iIndexLength):
        # Compare the 1st value to the 2nd value:
        if lUnsortedList[i] > lUnsortedList[i+1]:

            switch = lUnsortedList[i]
            lUnsortedList[i] = lUnsortedList[i+1]
            lUnsortedList[i+1] = switch
    iLengthList = iLengthList - 1

print(lUnsortedList)