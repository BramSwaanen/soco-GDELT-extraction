import pandas as pd
import os
import re
import csv

newspaper = "https://www.(publicceo|foxnews|pymnts|bbc)"
ai_regex = "-ai-|artificial-intelligence"

# Extract the header row from headers.csv WORKS
with open("headers.csv",'r') as file:
    header_string = file.read()
    header_list = header_string.split(",")
    header_list[-1] = header_list[-1][:-1]

print("header_list:", header_list)

# Loop over all data files in ./data
for path in os.listdir("./data"):
    print("********************")
    print(path)
    date,_ = path.split(".")
    # Save in a dataframe with header_list headers WORKS
    df = pd.read_csv(f"./data/{path}",names=header_list,sep="\t")
    print(df)
    # Extract relevant articles based on newspaper and ai_regex queries
    df = df[df.SOURCEURL.str.contains(newspaper)]
    print(df)
    print(df.SOURCEURL)
    df1 = df[df.SOURCEURL.str.contains(ai_regex)]
    print("df1:", df1.iloc[0].SOURCEURL)
    # TODO: get unique entries for SOURCEURL

    