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

# print("header_list:", header_list)

d = {}
# Loop over all data files in ./data
for path in os.listdir("./data"):
    # print("********************")
    # print(path)
    date,_ = path.split(".")
    # Save in a dataframe with header_list headers WORKS
    df = pd.read_csv(f"./data/{path}",names=header_list,sep="\t")
    # print(df)
    # Extract relevant rows based on newspaper and ai_regex queries WORKS
    df = df[df.SOURCEURL.str.contains(newspaper)]
    # print(df)
    # print(df.SOURCEURL)
    df1 = df[df.SOURCEURL.str.contains(ai_regex)]
    # print("df1:", df1.iloc[0].SOURCEURL)
    # Save the unique found urls in the dictionary under the current date
    unique_urls = df1.SOURCEURL.unique()
    # TODO: loop over unique urls and obtain necessary information right away
    # (see model on the back of LSA's coursework 3)
    d[date] = unique_urls
    
print(d)