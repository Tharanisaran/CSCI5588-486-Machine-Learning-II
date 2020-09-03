import numpy as np
import os
import collections

class HillClimbing:
    """ 
    Initializing the constants 
    STRING_LENGTH and NUMBER_OF_ITERATIONS 
    """
    def __init__(self):
        self.STRING_LENGTH = 40
        self.NUMBER_OF_ITERATIONS = 100
    
    """ 
    The below function creates a random array of 0's and 1's
    given the array length  
    """
    def CreateRandomArray(self,arsize):
        randarray = np.random.randint(2, size=arsize)
        return randarray
    
    """ 
    The below function calculates the fitness value for the given random array
    It counts the number of 1's in the given array and appies that in the function and returns
    the fitness value 
    """
    def CalculateFitness(self,arr):
        onescount = collections.Counter(arr)[1]
        return abs(13*onescount-170)
    
    """ 
    Given an array of length asize this function returns a array list of 
    one bit changed neighbours of length asize 
    """
    def getNeighbours(self,arr,asize): 
        neighbours = []
        for index in range(asize):
            temparr = list(arr)
            temparr[index] = 1 - arr[index]
            neighbours.append(temparr)
        return neighbours
    
    """ 
    Given a array list of arrays 
    this function returns calculates Fitness value for each array in the list and 
    returns the largest fitness value 
    """
    def GetLargestFV(self,arr):
        largestFV = 0
        for a in arr:
            currentFV = self.CalculateFitness(a)
            if currentFV > largestFV:
                largestFV = currentFV
                largestVN = a
        return largestVN

def main():
    hc = HillClimbing()
    
    for iteration in range(hc.NUMBER_OF_ITERATIONS):
        randomVC = hc.CreateRandomArray(hc.STRING_LENGTH)
        funtionvalueRandomVC = hc.CalculateFitness(randomVC)

        shouldIContinue = True

        while(shouldIContinue and (iteration < hc.NUMBER_OF_ITERATIONS)):
            
            neighbours = hc.getNeighbours(randomVC,hc.STRING_LENGTH)
            
            largestVN = hc.GetLargestFV(neighbours)

            functionValuelargestVN = hc.CalculateFitness(largestVN)

            if funtionvalueRandomVC < functionValuelargestVN:
                funtionvalueRandomVC = functionValuelargestVN
                randomVC = largestVN
            else:
                shouldIContinue = False
        
        if iteration < 99:
            print(funtionvalueRandomVC,end='')
            print(',',end='')
        else:
            print(funtionvalueRandomVC)

if __name__=="__main__":
    main()
