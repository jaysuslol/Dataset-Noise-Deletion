import os
import sys
import pandas as pd
import numpy as np

def IB2(ts):
    csvfile = pd.read_csv(os.getcwd() + '\\' + ts)
    df = pd.DataFrame(csvfile)

    cs = df.copy()
    for i in range(1, len(df)): # Keep first row as a random data point
        cs.drop(i, inplace=True)

    inherited = 1 # Number of inherited points (starting from 1 since we moved one datapoint from TS to CS)

    for i in range(len(df)):
        if (df.iloc[i, -1] == 'SKIP'): continue
        dfvalues = df.iloc[i][:]
        dfvalues = np.array(dfvalues)

        distances = []
        for j in range(len(cs)):
            if (i == j): continue

            csvalues = cs.iloc[j][:]
            csvalues = np.array(csvalues)

            # Calculate euclidean distance
            dist = np.sum((dfvalues[:-1] - csvalues[:-1])**2)**0.5 ## [:-1] avoids class names
            distances.append(dist)
            #print(dist)

        if (len(distances) > 0):
            distances = np.array(distances)
            #print(distances)
            neighbour = np.argmin(distances)
            #print(neighbour)
            if (cs.iloc[neighbour, -1] != df.iloc[i, -1]):
                #print(df.iloc[neighbour, -1])
                #print(df.iloc[i, -1])
                cs.loc[len(cs)] = dfvalues
                print('Moved datapoint with index ', i)
                inherited += 1
            
            #df.iloc[i, -1] = 'SKIP'
        
    IB2filename = os.path.splitext(ts)[0] + 'IB2.csv'
    cs.to_csv(IB2filename, index=False) ## Output: filenameIB2.csv
    print('Total inherited points: ', inherited)
        

def main():
    args = sys.argv[:]
    if (len(args) == 0 or len(args) > 2):
        print("Incorrect usage of arguments.\nUsage: python IB2Algorithm.py csvfile.csv")
        exit(-1)

    IB2(args[1])


if __name__ == '__main__':
    main()