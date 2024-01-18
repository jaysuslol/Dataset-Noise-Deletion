import pandas as pd
import sys
from sklearn.preprocessing import MinMaxScaler
import os

def normalizecsv(filename):
    csvfile = pd.read_csv(os.getcwd() + '\\' + filename) # Open .csv file
    df = pd.DataFrame(csvfile)  # Create dataframe of csv file
    classcol = df['class'] # Keep class column to concatenate it with normalized DF later

    #print(df) #debug

    scaler = MinMaxScaler() # Use default normalizing function (min:0, max:1)
    cols = df.columns[df.columns != 'class'] # Keep all columns except the one with the class names
    normalized_data = scaler.fit_transform(df[cols]) # Normalize remaining data using MinMaxScaler()

    normalized_df = pd.DataFrame(normalized_data, columns=cols) # Create a new dataframe to insert the normalized data into
    normalized_df = pd.concat([normalized_df, classcol], axis=1) # Concatenate normalized dataframe with class column

    normfilename = os.path.splitext(filename)[0] + '_normalized.csv'
    normalized_df.to_csv(normfilename, index=False)  ## Output: filename_normalized.csv


def main():
    args = sys.argv[:]
    if (len(args) == 0 or len(args) > 2):
        print("Incorrect usage of arguments.\nUsage: python NormalizeValues.py csvfile.csv")
        exit(-1)
    normalizecsv(args[1])


if __name__ == '__main__':
    main()