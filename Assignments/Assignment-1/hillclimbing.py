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
        self.MAX = 100
    
    """ 
    The below function creates a random array of 0's and 1's
    given the array size and how many ones you want in that array   
    """
    def CreateRandomArray(self,arsize,ones):
        onesArray = np.ones(ones, dtype=np.int)
        zerosArray = np.zeros(arsize-ones, dtype=np.int)
        wholeArray = np.concatenate((onesArray, zerosArray), axis = 0)
        np.random.shuffle(wholeArray)
        return wholeArray
    
    """ 
    The below function calculates the fitness value for the given random array
    It counts the number of 1's in the given array and applies that in the function and returns
    the fitness value 
    """
    def CalculateFitness(self,onescount):
        return abs(13*onescount-170)

    def getOnesCount(self,arr):
        return collections.Counter(arr)[1]
    
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
            currentOnesCount = self.getOnesCount(a)
            currentFV = self.CalculateFitness(currentOnesCount)
            if currentFV > largestFV:
                largestFV = currentFV
                largestVN = a
        return largestVN

def main():
    hc = HillClimbing()
    #reset the algorithm for MAX times
    t = 0
    while t < hc.MAX:
        """
        Selection of random array with zero's and one's evenly distributed to get the 
        Global maximum value and Local Maximum value
        """
        if t%2 == 0:
            randomVC = hc.CreateRandomArray(hc.STRING_LENGTH,np.random.randint(0,20))
        else: 
            randomVC = hc.CreateRandomArray(hc.STRING_LENGTH,np.random.randint(20,hc.STRING_LENGTH))
        """
        Calculating the number of ones for the random VC and Evaluating the fitness value 
        for VC
        """
        randomOnescount = hc.getOnesCount(randomVC)
        funtionvalueRandomVC = hc.CalculateFitness(randomOnescount)

        local = False
        while(not(local) and (t < hc.MAX)):  
            neighbours = hc.getNeighbours(randomVC,hc.STRING_LENGTH)
            largestVN = hc.GetLargestFV(neighbours)
            onesCountLargestVN = hc.getOnesCount(largestVN)
            functionValuelargestVN = hc.CalculateFitness(onesCountLargestVN)
            if funtionvalueRandomVC < functionValuelargestVN:
                funtionvalueRandomVC = functionValuelargestVN
                randomVC = largestVN
            else:
                local = True
        if t < 99:
            print(funtionvalueRandomVC,end='')
            print(',',end='')
        else:
            print(funtionvalueRandomVC)
        t += 1

if __name__=="__main__":
    main()
