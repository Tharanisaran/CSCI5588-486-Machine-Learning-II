import os

# class GeneticAlgorithm():
#     def __init__(self):
#         pass
#     def GA_Main(self):
#         print("Something")

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
    print(list(zip(seqValues,fitnessValues)))

if __name__ == '__main__':
    main()               