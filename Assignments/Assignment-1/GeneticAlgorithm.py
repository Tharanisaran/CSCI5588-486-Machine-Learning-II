import os
import random 
import operator


class GeneticAlgorithm:
    def __init__(self):
        """
        1. Initialize the Population 
        """
        self.populationList= []
        self.crossoverPopulation = []
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
    """
    Given a chromosome this function calculates and returns the fitness value
    """
    def calculateFitness(self,chromosome):
        chromosome_dict={}
        fitness=0
        for indexposition,chromosomedata in enumerate(chromosome):
            chromosome_dict[chromosomedata[1]]=(indexposition,chromosomedata[0])

        for key,value in chromosome_dict.items():
            #get the fitness value if there is a topological neighbour in right
            fitness = fitness + self.individualFitness(key,(key[0]+1,key[1]),chromosome_dict)
            #get the fitness value if there is a topological neighbour in left
            fitness = fitness + self.individualFitness(key,(key[0]-1,key[1]),chromosome_dict)
            #get the fitness value if there is a topological neighbour in up
            fitness = fitness + self.individualFitness(key,(key[0],key[1]+1),chromosome_dict)
            #get the fitness value if there is a topological neighbour in down
            fitness = fitness + self.individualFitness(key,(key[0],key[1]-1),chromosome_dict)
        return fitness
    """
    This function returns the individual fitness at a selected axis by comparing
    the topological neighbours 
    """
    def individualFitness(self,baseAxis,neighbourAxis,chromosome_dict):
        #if the neighbouraxis is part of the chromosome orientation
        if neighbourAxis in chromosome_dict:
            baseGene=chromosome_dict[baseAxis]
            neighbourGene=chromosome_dict[neighbourAxis]
            # checking the topological neighbours in ascending order and eliminating the covalent bonded neighbours 
            if (baseGene[0]<neighbourGene[0]) and (abs(baseGene[0]-neighbourGene[0])>1):
                if baseGene[1]==0 and neighbourGene[1]==0:
                    return 1
        return 0 
    
    def rouletteWheelSelection(self,beforeCrossoverPopulation):
        max=0
        current=0
        for i in beforeCrossoverPopulation:
            max+=i[1]
        selection=random.randint(0,max)
        for i in beforeCrossoverPopulation:
            current+=i[1]
            if current>selection:
                return i[0]
    
    def crossover(self,selectedChromosomes,crossoverPosition):
        chromosome1 = selectedChromosomes[0]
        chromosome2 = selectedChromosomes[1]
        # print(chromosome1,chromosome2,crossoverPosition)
        partOfChromosome1=chromosome1[:crossoverPosition+1]
        partOfChromosome2=chromosome2[crossoverPosition+1:]
        partOfChromosome1Axes={i[1] for i in partOfChromosome1}

        #Detecting Previous Direction
        prevDir = None

        Ax = [0,0,0]
        Ay = [0,0,0]

        if chromosome1[crossoverPosition][1][1]==chromosome1[crossoverPosition-1][1][1]:
            if (chromosome1[crossoverPosition-1][1][0] - chromosome1[crossoverPosition][1][0]) == 1:
                prevDir = 'RIGHT'
            else:
                prevDir = 'LEFT'
        else: 
            if (chromosome1[crossoverPosition-1][1][1] - chromosome1[crossoverPosition][1][1]) == 1:
                prevDir = 'UP'
            else:
                prevDir = 'DOWN'
        
        if prevDir == 'RIGHT':
            Ax = [-1,0,0]
            Ay = [0,1,-1]
        elif prevDir == 'LEFT':
            Ax = [1,0,0]
            Ay = [0,1,-1]
        elif prevDir == 'UP':
            Ax = [1,-1,0]
            Ay = [0,0,-1]
        elif prevDir == 'DOWN':
            Ax = [1,-1,0]
            Ay = [0,0,1]

        for rotate in range(3):
            crossoverList = partOfChromosome2
            crossover_Xdir = chromosome1[crossoverPosition][1][0]+Ax[rotate] - chromosome2[crossoverPosition+1][1][0]
            crossover_Ydir = chromosome1[crossoverPosition][1][1]+Ay[rotate] - chromosome2[crossoverPosition+1][1][1]

            crossoverList[0] = (crossoverList[0][0],(chromosome1[crossoverPosition][1][0]+Ax[rotate],chromosome1[crossoverPosition][1][1]+Ay[rotate])) 

            for j in range(len(crossoverList)-1):
                crossoverList[j+1] = (chromosome2[crossoverPosition+j+2][0],(chromosome2[crossoverPosition+j+2][1][0]+ crossover_Xdir ,chromosome2[crossoverPosition+j+2][1][1]+ crossover_Ydir)) 

            crossover_Axes = {a[1] for a in crossoverList}

            if not self.collision(partOfChromosome1Axes,crossover_Axes):
                return partOfChromosome1 + crossoverList

            elif rotate == 2: 
                return None

    def collision(self,axes1,axes2):
        for axis in axes2:
            if axis in axes1:
                return True
        return False

    def GA_Main(self,proteinList):
        sequence=proteinList[0][0]
        fitness=proteinList[0][1]
        # print(sequence)
        # print(fitness)
        chromosomeList = []
        binarySequence=self.getBinarySequence(sequence)

        while (len(chromosomeList)<200):
            try:
                chromosomeList.append(self.chromosomeOrientation(binarySequence))
            # When there is situation of collision while forming chromosome randomly, Indexerror occurs 
            # I catch the exception and drop that structure 
            except IndexError:
                print("No Valid Options to select")
                continue
        """
        2. Compute Fitness of Population for all Chromosome Ci
        """
        for chromosome in chromosomeList:
            self.populationList.append((chromosome, self.calculateFitness(chromosome)))
        # print(self.populationList[0])
        """
        3. Sort the Population in descending order based on their fitness 
        """
        self.populationListSorted = sorted(self.populationList,key=operator.itemgetter(1),reverse=True)
        # print(self.populationListSorted[0])
        """ 
        4. Examine: C1/Progress or Max_gen, Exit Condition 
        """

        """
        5. Taken 10% of Elite and form a New Population 
        """
        self.elitePopulation = self.populationListSorted[:20]

        """
        6. 80% crossover chromosomes and fill the New Population 
        """
        beforeCrossoverPopulation = self.populationListSorted[20:180]
        while (len(self.crossoverPopulation)<160):
            try: 
                selectedChromosomes=[]
                for i in range(2):
                    selectedChromosomes.append(self.rouletteWheelSelection(beforeCrossoverPopulation))
                crossoverResult=self.crossover(selectedChromosomes,random.randint(1,len(selectedChromosomes[0])-2))

                if not (crossoverResult==None):
                    self.crossoverPopulation.append((crossoverResult,self.calculateFitness(crossoverResult)))
            except Exception as e:
                print(e)
                continue

        
        print(self.crossoverPopulation)
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
    