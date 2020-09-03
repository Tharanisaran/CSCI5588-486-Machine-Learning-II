import numpy as np
import os
import collections

class HillClimbing:
    def __init__(self):
        pass
    
    def CreateRandomArray(self,arsize):
        randarray = np.random.randint(2, size=arsize)
        return randarray

    def CalculateFitness(self,ones_count):
        return abs(13*ones_count-170)
        
	
    def GetOnesCount(self,arr):
	    return collections.Counter(arr)[1]

    def GetNeighbour(self,index,arr):
        temparr = list(arr) 
        val = arr[index]
        temparr[index] = 1 - val
        return temparr



def main():
    hc = HillClimbing()
    
    for turn in range(100):
        arraySize = 40
        pointarray = hc.CreateRandomArray(arraySize)
        onesCount = hc.GetOnesCount(pointarray)
        MaxFitness = hc.CalculateFitness(onesCount)
        # print(hc.GetNeighbour(0,arr))

        for i in range(arraySize):
            print("Original Array: %s"%(str(pointarray)))
            currNeighbour = hc.GetNeighbour(i,pointarray)
            onesCount = hc.GetOnesCount(currNeighbour)
            print("Neighbour Index %s : %s Onescount:%s"%(str(i),str(currNeighbour),str(onesCount)))
            neighbourFitness = hc.CalculateFitness(onesCount)
            if neighbourFitness > MaxFitness:
                MaxFitness = neighbourFitness

        print("Turn: %s - Final Max: %s"%(str(turn),str(MaxFitness)))

    # max=0
    # while(max<2):
    #     arr = hc.CreateRandomArray(40)
    #     print(arr)
        # ones_count=counting_ones(arr)
        # print(ones_count)
    """" current_fitness=fitness(ones_count)
		print(current_fitness)
		max+=1
		neighbor_index=np.random.randint(0,len(arr)-1)
		print(neighbor_index)
		for i in range(len(arr)):
			if i==neighbor_index:
				if arr[i]==0:
					arr[i]=1
				else:
					arr[i]=0
			else:
				arr2.append(arr[i])
		print(arr2) """

if __name__=="__main__":
    main()

	
					

