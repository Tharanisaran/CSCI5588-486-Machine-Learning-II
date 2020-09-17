import os
import random 


class GeneticAlgorithm:
    def __init__(self):
        self.populationList=[]
    """ 
    Input: Sequence text with hphphp....hhhppp
    Output: List [0,1,0,1,0,1,....,0,0,0,1,1,1]
    
    Function modifies the amino acid sequence into a binary 
    sequence by replacing h with 0 and p with 1
    """
    def getBinarySequence(self,sequence):
        binarySequence=[]
        for gene in sequence:
            if gene=='h':
                binarySequence.append(0)
            else:
                binarySequence.append(1)
        return binarySequence

    """ 
    This module generates the Chromosome Orientation/structure in Random for the given sequence 
    Input: [gene1,gene2,....,gene_N]
    Output: [(gene1, (X1, Y1)), (gene2, (X2, Y2)), ...., (gene_N, (Xn, Yn))]
    """
    def chromosomeOrientation(self,binarySequence):
        #Assigning the first value of binary sequence to (0,0) position initially
        currentPosition=(0,0)
        chromosome=[(binarySequence[0],currentPosition)]
        #Creating a dictionary to store assigned coordinates
        assignedCoordinates={currentPosition}
        for gene in binarySequence[1:]:
            allOptions=[]
            validOptions=[]
            # Adding the right direction option
            allOptions.append((currentPosition[0]+1,currentPosition[1]))
            # Adding the left direction option
            allOptions.append((currentPosition[0]-1,currentPosition[1]))
            # Adding the Up direction option 
            allOptions.append((currentPosition[0],currentPosition[1]+1))
            # Adding the Down direction option 
            allOptions.append((currentPosition[0],currentPosition[1]-1))

            # filtering valid options from allOptions  
            for axis in allOptions:
                if axis not in assignedCoordinates:
                    validOptions.append(axis)
            # Select one Valid position in random and assign the gene as it's position and move forward with the orientation 
            forwardPosition = random.choice(validOptions)
            chromosome.append((gene, forwardPosition))
            assignedCoordinates.add(forwardPosition)
            currentPosition = forwardPosition
        return chromosome
    def calculateFitness(self,chromosome):
        chromosome_dict={}
        fitness=0
        for indexposition,chromosomedata in enumerate(chromosome):
            chromosome_dict[chromosomedata[1]]=(indexposition,chromosomedata[0])
        for key,value in chromosome_dict.items():
            fitness = fitness + self.individualFitness(key,(key[0]+1,key[1]),chromosome_dict)

            fitness = fitness + self.individualFitness(key,(key[0]-1,key[1]),chromosome_dict)

            fitness = fitness + self.individualFitness(key,(key[0],key[1]+1),chromosome_dict)

            fitness = fitness + self.individualFitness(key,(key[0],key[1]-1),chromosome_dict)
        return fitness
    
    def individualFitness(self,baseAxis,neighbourAxis,chromosome_dict):
        if neighbourAxis in chromosome_dict:
            baseGene=chromosome_dict[baseAxis]
            neighbourGene=chromosome_dict[neighbourAxis]
            if (baseGene[0]<neighbourGene[0]) and (abs(baseGene[0]-neighbourGene[0])>1):
                if baseGene[1]==0 and neighbourGene[1]==0:
                    return 1
        return 0 


    def GA_Main(self,proteinList):
        sequence=proteinList[0][0]
        fitness=proteinList[0][1]
        # print(sequence)
        # print(fitness)
        """
        1. Initialize the Population 
        """
        binarySequence=self.getBinarySequence(sequence)
        chromosome=self.chromosomeOrientation(binarySequence)
        print(chromosome)
        """
        2. Compute Fitness of Population for all Chromosome Ci
        """
        print(self.calculateFitness(chromosome))
        """
        3. Sort the Population  
        """
        """ 
        4. Examine: C1/Progress or Max_gen, Exit Condition 
        """

        """
        5. Take 5 to 10% of Elite and form a New Population 
        """

        """
        6. 80% crossover chromosomes and fill the New Population 
        """
        """ 
        7. Fillup Pop2 randomly
        """
        """ 
        8. Mutate the 5% to 50% Non elite chromosome in the 
        population1 and fill it in Pop2  
        """
        """ 
        9.Increase Generation and Goto Step2
        """


def main():
    with open("C:\\data\\tharugit\\CSCI5588-486-Machine-Learning-II\\Assignments\\Assignment-1\\Input.txt") as f:
        content = f.readlines()
    seqValues = []
    fitnessValues = []
    contents = [x.strip() for x in content]
    for line in contents:
        if len(line)>0:
            if "Comment" in line:
                continue
            if "Seq" in line:
                seqValues.append(line.replace("Seq = ",""))
            if "Fitness =" in line:
                fitnessValues.append(abs(int(line.replace("Fitness = ",""))))
    GeneticAlgorithm().GA_Main(list(zip(seqValues,fitnessValues)))

if __name__ == '__main__':
    main()               
    