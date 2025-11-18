# #Helper method to sort the ratio values
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    #Recursively break into sorted halves
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft,sortedRight)

def merge(left, right):
    result = []
    indexes = []
    i, j = 0,0

    #Compares each element, and adds the largest element to the beginning of the list
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    #Handles the largest values
    result.extend(left[i:])
    result.extend(right[j:])

    return result
    

def FractionalNapsackProblem(values, weights):
    #Create an array to represent value/weight ratio
    ratios = []
    for i in range(values):
        ratios[i] = values[i] / weights[i]
    
    #Sort the array from ascending to descending
    ratios = mergeSort(ratios)

    #Now that the ratios are sorted, do the fractional napsack problem
    remaining = 1.0
    i = 0
    value = 0
    while remaining > 0 and i < len(values):
        value += ratios[i] * weights

    

#Test if mergesort works
print(mergeSort([1,2,3,4,5,99,4,71,17,24,2,5,6]))