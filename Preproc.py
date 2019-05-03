<<<<<<< Updated upstream
=======
<<<<<<< HEAD
import io
import pandas as pd

trainingFrame = pd.read_csv("trainData.tsv", sep='\t')

def refineDict(_dict, *retainedKeys):
    try:
        rKeys = [k for k in retainedKeys]
        for key in list(_dict):
            if key not in rKeys:
                del _dict[key]
        if not len(_dict) == 0:
            return _dict
        else:
            raise KeyError('String arguments were not passed to `itercolumns` argument: *colName')
    except KeyError:
        print('Type `help(itercolumns)` for suggested usage'

def itercolumns(dataframe, *colName, _aslist=False, _asdict=True):
    if len(colName) == 1:
        match = colName[0]
        for frame in dataframe.itertuples():
            columnsList = frame._asdict()
            columnsList = dict(columnsList)
            i = 0
            while i < len(columnsList):
                if list(columnsList)[i] == match:
                    return i
                i += 1
            break
        raise ValueError('DataFrame did not contain specified column header name')

    if all([_aslist == True]):
        return list(dataframe)

    else:
        if all([_aslist == False, _asdict == True]):
            for frame in dataframe.itertuples():
                columnsList = frame._asdict()
                columnsList = dict(columnsList)
                columnsDict = OrderedDict()
                i = 0
                for col in list(columnsList):
                    columnsDict[col] = i
                    i += 1
                if len(colName) == 0:
                    return columnsDict
                elif len(colName) >= 1:
                    for argGiven in colName:
                        if argGiven not in columnsList:
                            raise ValueError('Dataframe did not contain specified column header name')
                    return refineDict(columnsDict, *[x for x in colName])


trainingFrame.columns = trainingFrame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
trainingFrame = trainingFrame[~trainingFrame.gene_description.str.contains("(endogenous control)")]
#trainingFrame = trainingFrame[trainingFrame.index.duplicated()]

allA = trainingFrame
allA = allA.filter(like='call')

allA = allA.filter(items=['M','P'], axis=0 )
filteredDF = pd.DataFrame()

# trainingFrame = trainingFrame[(trainingFrame == 'M')|(trainingFrame == 'P')].dropna()

# ['call', 'call.1', 'call.2', 'call.3', 'call.4', 'call.5', 'call.6', 'call.7', 'call.8', 'call.9', 'call.10', 'call.11', 'call.12', 'call.13',
#  'call.14', 'call.15', 'call.16', 'call.17', 'call.18', 'call.19', 'call.20', 'call.21', 'call.22', 'call.23', 'call.24', 'call.25',
#  'call.26', 'call.27', 'call.28', 'call.29', 'call.30', 'call.31', 'call.32', 'call.33', 'call.34', 'call.35', 'call.36', 'call']

# for index, row in trainingFrame.iterrows():
#     for item in row:
#         if item == 'P' or item =='M':
#             filteredDF.append(row)
#             break
x = lambda j: [frame for frame in trainingFrame.itertuples()]
'''



# print(trainingFrame)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(trainingFrame)
#print(allA)
'''
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
writeToFile(data, clsFile)
=======
writeToFile(data, clsFile)
>>>>>>> origin/master
>>>>>>> Stashed changes
