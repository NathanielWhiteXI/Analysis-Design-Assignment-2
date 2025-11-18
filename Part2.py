#Helper method provided by assignment. It was modified to be more useful for this implementation.
def getDigit(num, digit):
    return (num // digit) % 10

#Additional stable sorting algorithm to properly order digits
def countingSort(arr, column):
    n = len(arr)
    
    #Use whack python syntax to create necessary arrays.
    output = [0] * n
    count  = [0] * 10

    #Populate counting array
    for i in range(n):
        count[getDigit(arr[i], column)] += 1
    
    #Change the count array to include the cumulative sum.
    for i in range(1,10):
        count[i] += count [i - 1]

    #Handles the output array
    i = n - 1
    #Builds output array in reverse to maintain stability.
    while i >= 0:
        output[count[getDigit(arr[i], column)]-1] = arr[i]
        count[getDigit(arr[i],column)] -= 1
        i -= 1
    
    return output

def radixSort(arr):
    #Max is used to compute number of necessary columns to work on
    maximum = max(arr)

    #Exponent used to control which column is worked on.
    exp = 1
    while maximum/exp >= 1:
        arr = countingSort(arr, exp)
        exp *= 10
    return arr

#Test Code
arr = [58, 260, 1, 52, 35, 964, 73, 123, 7]
print(arr)
print(radixSort(arr))

