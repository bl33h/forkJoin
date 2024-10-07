# Copyright (C), 2024-2025, bl33h 
# FileName: main.py
# Author: Sara Echeverria
# Version: I
# Creation: 05/10/2024
# Last modification: 06/10/2024

import concurrent.futures

# --- sum the elements of a sublist ---
def sumList(sublist):
    return sum(sublist)

# --- fork join pattern ---
def forkJoinSum(numElements, numSublists):
    # list of numbers from 1 to numElements
    fullList = list(range(1, numElements + 1)) 
    
    # ensures even division 
    sublistSize = (len(fullList) + numSublists - 1) // numSublists  
    sublists = [fullList[i * sublistSize:(i + 1) * sublistSize] for i in range(numSublists)]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(sumList, sublists))
    
    return sum(results)

# --- main method ---
def main():
    totalSum = forkJoinSum(100, 5)  
    print("-> total sum:", totalSum)

if __name__ == "__main__":
    main()