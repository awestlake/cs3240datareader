#Alexa Westlake CMPS 3240 Machine Learning Project

#This is a data reader that will read my data into an array of parameters, the parameters are also arrays


import csv
from collections import defaultdict


#here is a list of my csv files
figuresList = ["98246-instant.csv"]
#these are each arrays that represent a sample
jan11 = []
april11 = []
july11 = []
oct11 = []
jan12 = []
april12 = []
july12 = []
oct12 = []
jan13 = []
april13 = []
july13 = []
oct13 = []
jan14 = []
april14 = []
july14 = []
oct14 = []
jan15 = []
april15 = []
july15 = []
oct15 = []
jan16 = []
april16 = []
july16 = []
oct16 = []
jan17 = []
april17 = []

#creation of the 2D arary of samples

for figure in figuresList:
    with open(figure, newline='') as csvfile:
        #this is called tiffany becasue the company I am predicting is Tiffany & Co
          tiffany = csv.reader(csvfile, delimiter='?', quotechar='|')
          for row in tiffany:
              #put the data in a list, makes indexing possible
            row = ','.join(row)
            row = row.split(',')
              #features are each of the row in a balance sheet, each colomn contains all the features of one sample
            jan11 += [row[1]]
            april11 += [row[2]]
            july11 += [row[3]]
            oct11 += [row[4]]
            jan12 += [row[5]]
            april12 += [row[6]]
            july12 += [row[7]]
            oct12 += [row[8]]
            jan13 += [row[9]]
            april13 += [row[10]]
            july13 += [row[11]]
            oct13 += [row[12]]
            jan14 += [row[13]]
            april14 += [row[14]]
            july14 += [row[15]]
            oct14 += [row[16]]
            jan15 += [row[17]]
            april15 += [row[18]]
            july15 += [row[19]]
            oct15 += [row[20]]
            jan16 += [row[21]]
            april16 += [row[22]]
            july16 += [row[23]]
            oct16 += [row[24]]
            jan17 += [row[25]]
            april17 += [row[26]]

