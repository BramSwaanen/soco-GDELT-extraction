import pandas as pd
import os
import re
import csv
import json
import requests
from bs4 import BeautifulSoup
from html import parser

def extract_content(url:str):
    '''
    Extracts content from a news website indicated by url
    '''
    req = requests.get(url)
    soup = BeautifulSoup(req.content,'html.parser')
    contents = []
    for script in soup.find_all("script"):
        try:
            if script['type'] == 'application/ld+json':
                contents.append(json.loads(script.contents[0]))
        except:
            pass
    # print("contents:",contents)
    # date = contents[0]['datePublished']
    headline = contents[0]['headline']
    mainText = contents[0]['articleBody']
    return headline, mainText

newspaper_regex = "https://www.(foxnews|cnn|cbsnews|nbcnews)" # The pipeline has been tested for all these sites
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
    # Extract relevant rows based on newspaper_regex and ai_regex queries WORKS
    df = df[df.SOURCEURL.str.contains(newspaper_regex)]
    # print(df)
    # print(df.SOURCEURL)
    df1 = df[df.SOURCEURL.str.contains(ai_regex)]
    # print("df1:", df1.iloc[0].SOURCEURL)
    # Save the unique found urls in the dictionary under the current date
    unique_urls = df1.SOURCEURL.unique()
    # TODO: loop over unique urls and obtain necessary information right away
    # (see model on the back of LSA's coursework 3)
    print("length unique_urls:", len(unique_urls))

    # Option 1
    # for nr,url in enumerate(unique_urls):
    #     headLine,mainText = extract_content(url)
    #     matches = re.match(newspaper_regex,url)
    #     newspaper = matches.group()[12:]
    #     d[f"{date}-{nr}"] = newspaper,headLine,mainText

    # Option 2
    multiple_pages = {}
    for index, url in enumerate(unique_urls):
        headLine,mainText = extract_content(url)
        matches = re.match(newspaper_regex,url)
        newsPaper = matches.group()[12:]
        multiple_pages[str(index)] = {"newsPaper":newsPaper,"headLine":headLine,"mainText":mainText}
    d[date] = multiple_pages
    # TODO: think of the best way to identify a same date's different articles. This can
    # either be done with a different key (option 1) or by zipping the different articles together
    # in a dictionar under the same key with an index (option 2). I personally think option 2 is
    # better.

print(len(d["20240429"]))