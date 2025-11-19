# # #Helper method to sort the ratio values
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
    i, j = 0,0

    #Compares each element, the element with the largest ratio is sorted.
    while i < len(left) and j < len(right):
        if left[i][0]/left[i][1] > right[j][0]/right[j][1]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #Handles the smallest remaining values
    result.extend(left[i:])
    result.extend(right[j:])

    return result
    

def fractionalNapsackProblem(values, weights):
    #Create an array to represent value/weight ratio
    ratios = [[values[i], weights[i]] for i in range(len(values))]
    #Sort from ascending to descending
    ratios = mergeSort(ratios)
    
    #Use the max weight in percentage to calculate the max amount we can take
    totalValue = 0.0
    remainingWeight = 1.0
    i = 0
    #While there are still objects and weight
    while remainingWeight > 0.0 and i < len(ratios):
        # print(totalValue)
        #If there is insufficient weight, drop it
        if remainingWeight < ratios[i][1]:
            pass
        #Otherwise, add it to the bag
        else:
            print(ratios[i])
            totalValue += ratios[i][0]
            remainingWeight -= ratios[i][1]
        i += 1
    return totalValue
    

#Test if mergesort works
print(fractionalNapsackProblem([100, 25, 7, 8, 13, 250, 13, 62, 97], [0.1, 0.5, 0.2, 0.1, 0.1, 0.6, 0.5, 0.2, 0.5]))