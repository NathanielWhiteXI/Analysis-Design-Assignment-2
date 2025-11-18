#Part 1 Solution
def minEditDistance(str1, str2, len1, len2):
    #Check if either str is empty. This is to deal with strings that are complety different, and our base case.
    if len1 == 0:
        return len2
    
    if len2 == 0:
        return len1
    
    #If the ends are the same, we can use this.
    if str1[len1-1] == str2[len2-1]:
        return minEditDistance(str1, str2, len1 - 1, len2 - 1)

    #Otherwise, recursively determine the smallest permutation of edits.   
    return 1 + min(minEditDistance(str1, str2, len1, len2 - 1), minEditDistance(str1, str2, len1 - 1, len2), minEditDistance(str1, str2, len1 - 1, len2 - 1))


print(minEditDistance("cabbage", "merchant", len("cabbage"), len("merchant")))
