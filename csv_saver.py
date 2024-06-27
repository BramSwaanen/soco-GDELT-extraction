import pandas as pd
import os
import re
import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_content(url:str):
    '''
    Extracts content from a news website indicated by url
    '''
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        contents = []
        for script in soup.find_all("script"):
            try:
                if script['type'] == 'application/ld+json':
                    contents.append(json.loads(script.contents[0]))
            except:
                pass
        headline = contents[0]['headline']
        mainText = contents[0]['articleBody']
        return headline, mainText
    except Exception as message:
        if not os.path.exists("./errors"):
            os.mkdir("./errors")
        with open(f"./errors/loading-errors.txt","a") as file:
            file.write(f"Error loading {url}:\n{str(message)}\n\n")
        return None, None

newspaper_regex = "https://www.(?:foxnews|cnn|cbsnews|nbcnews)"
ai_regex = "-ai-|artificial-intelligence|gpt|natural-language-processing|chatbot|speech-recognition"
data_path = "./data"

# Extract the header row from headers.csv
with open("headers.csv",'r') as file:
    header_string = file.read()
    header_list = header_string.split(",")
    header_list[-1] = header_list[-1].strip()

d = {}
articles_data = []  # List to collect all articles data for CSV export

# Loop over all data files in data_path
len_dir = len(os.listdir(data_path))
counter = 0
for path in os.listdir(data_path):
    counter += 1
    print(f"file {counter} of {len_dir}",end="\r")
    date, _ = path.split(".")
    try:
        df = pd.read_csv(f"{data_path}/{path}", names=header_list, sep="\t", low_memory=False) # read csv-file
    except Exception as message:
        with open("./errors/loading-errors.txt","a") as file:
            file.write(f"Error reading {path}:\n{message}\n\n")
    try:
        df = df[df.SOURCEURL.str.contains(newspaper_regex)] # filter df urls on newspaper_regex
    except Exception as message:
        with open("./errors/loading-errors.txt","a") as file:
            file.write(f"Error reading {path}:\n{message}\n\n")
    try:
        df1 = df[df.SOURCEURL.str.contains(ai_regex)] # filter df urls on ai_regex
    except Exception as message:
        with open("./errors/loading-errors.txt","a") as file:
            file.write(f"Error reading {path}:\n{message}\n\n")

    unique_urls = df1.SOURCEURL.unique()

    for index, url in enumerate(unique_urls):
        headline, mainText = extract_content(url)
        if headline:
            matches = re.match(newspaper_regex, url)
            newsPaper = matches.group()[12:]  # Extracting newspaper name from the URL
            article_info = {
                "Date": date,
                "NewsPaper": newsPaper,
                "Headline": headline,
                "MainText": mainText
            }
            articles_data.append(article_info)  # Append each article's data to the list

# Creating DataFrame from the list of article data
articles_df = pd.DataFrame(articles_data)
articles_df.to_csv("extracted_articles.csv", index=False)
print("Data saved to 'extracted_articles.csv'.")
