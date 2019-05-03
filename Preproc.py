import io
import pandas as pd

def preprocess(trainingFrame):
    data = trainingFrame.values.tolist()

    threshold = 20
    # array of genes to be removed
    remove = []
    for gene in data:
        # present is false until one "P" or "M" is found
        present = False
        # min and max expression values
        min = threshold
        max = threshold
        for val in range(2, len(gene)):
            # odd values are "A", "P", or "M"
            if val % 2 == 1:
                if gene[val] == "P" or gene[val] == "M":
                    present = True
            # even values are the expression values
            else:
                # if expression value less than threshold set to threshold
                if gene[val] < threshold:
                    gene[val] = threshold
                if gene[val] < min:
                    min = gene[val]
                if gene[val] > max:
                    max = gene[val]
        # if all "A" remove gene
        if present == False:
            remove.append(gene)
        # if less than 2 fold change remove gene
        elif (2 * min) > max:
            remove.append(gene)

    for gene in remove:
        data.remove(gene)

    return data

def writeToFile(data, clsFile):
    vector = open(clsFile)
    temp = vector.readline()
    ALLorAML = vector.readline()
    ALLorAML = ALLorAML.split(" ")
    if "\n" in ALLorAML:
        ALLorAML.remove("\n")
    output = str(trainingFrame.columns[1])
    for expNum in range(1, len(ALLorAML) + 1):
        output += "\tExp" + str(expNum)
    output += "\n \t"
    for exp in ALLorAML:
        # 0 is ALL, 1 is AML
        if int(exp) == 0:
            output += "(ALL)\t"
        else:
            output += "(AML)\t"
    output += "\n"
    for gene in data:
        output += gene[1] + "\t"
        for val in range(2, len(gene)):
            # even values are the expression values
            if val % 2 == 0:
                output += str(gene[val]) + "\t"
        output += "\n"

    preprocessedData = open("preprocessedData.tsv", "w")
    preprocessedData.writelines(output)

trainingFrame = pd.read_csv("trainData.tsv", sep='\t')

trainingFrame.columns = trainingFrame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
trainingFrame = trainingFrame[~trainingFrame.gene_description.str.contains("(endogenous control)")]

data = preprocess(trainingFrame)
clsFile = "ALL_vs_AML_train_set_38_sorted.cls"
writeToFile(data, clsFile) 