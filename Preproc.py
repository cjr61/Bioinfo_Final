import io
import pandas as pd

trainingFrame = pd.read_csv("trainData.tsv", sep='\t')


trainingFrame.columns = trainingFrame.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
trainingFrame = trainingFrame[~trainingFrame.gene_description.str.contains("(endogenous control)")]

print(trainingFrame)