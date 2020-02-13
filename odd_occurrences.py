"""
Write a function that will be given a list of integers as a parameter. 
It is KNOWN that exactly one number in the list occurs an odd number of times 
(no input validation necessary). 
The function should return that number.  E.g. F (<2, 3, 3, 2, 2>) = 2 
""" 
 
import functools


def odd_occurrence_xor(arr):    
    """
    
    Reduce the list by using the XOR operator.
    We pass through the list once, and store only one value.
    Space complexity: $O(1)$; Time complexity: $O(n)$.

    Parameters
    ----------
    arr : integer

    Returns
    -------
    integer

    """
    return functools.reduce(lambda x,y: x^y, arr)


def odd_occurence_hashmap(arr):
    """
    
    Implement the solution by using a hashmap.
    We iterate through the list once, and store every value that we encounter,
    then iterate through our hashmap/dictionary structure once.
    Space complexity: $O(n)$; Time complexity: $O(n)$.
    
    Parameters
    ----------
    arr : integer

    Returns
    -------
    key : integer

    """
    hashmap = dict()
    for num in arr:
        if num in hashmap.keys():
            hashmap[num] = (hashmap[num] + 1) % 2
        else:
            hashmap[num] = 1
    for key in hashmap.keys():
        if hashmap[key] == 1:
            return key