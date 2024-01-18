import sys
import os
import pandas as pd
import numpy as np
from collections import Counter


def ENN(ts, k):
    csvfile = pd.read_csv(os.getcwd() + '\\' + ts)
    df = pd.DataFrame(csvfile)
    es = csvfile
    esdf = pd.DataFrame(es)
    rows = len(df) # Assuming there are no missing values

    removed = 0 # Number of removed points

    #print(rows) #debug, prints 150

    for i in range(0, rows):
        ivalues = df.iloc[i][:]
        ivalues = np.array(ivalues)

        distances = []

        """
        for j in range(0, rows):
            if (i == j): continue

            jvalues = df.iloc[j][:]
            jvalues = np.array(jvalues)

            # Calculate euclidean distance
            dist = np.sum((ivalues[:-1] - jvalues[:-1])**2)**0.5 ## [:-1] avoids class names
            #distances.append([dist, jvalues[-1]]) ## jvalues[-1] is the class name
            distances.append(dist)
        """
        distances = np.array(distances)
        distances = distances.argpartition(k) ## Sort only by 3 smallest
        k_neighbors = distances[:k] ## Find k-neighbours
        majority = []

        #print(k_neighbors)

        #for j in range(0, k):
            #k_neighbors.append(distances[distances[j]])
        
        for j in range(0, k):
            majority.append(df.iloc[k_neighbors[j], -1])

        #print(majority)
        if (len(majority) != len(set(majority))):
            count = Counter(majority).most_common(1) ## Count is a dictionary
            print(count)

            if (count[0][0] != ivalues[-1]):
                esdf.drop(i, inplace=True)
                print('Removed point with index ', i)
                removed += 1     
            
    ENNfilename = os.path.splitext(ts)[0] + 'ENN.csv'
    esdf.to_csv(ENNfilename, index=False) ## Output: filenameENN.csv
    print('Total removed points: ', removed)
    print('Remaining points: ', rows-removed)



def main():
    args = sys.argv[:]
    if (len(args) == 0 or len(args) > 3):
        print("Incorrect usage of arguments.\nUsage: python ENNAlgorithm.py csvfile.csv K (default: 3)")
        exit(-1)

    if (len(args) == 2):
        ENN(args[1], 3)
    else:
        ENN(args[1], args[2])


if __name__ == '__main__':
    main()