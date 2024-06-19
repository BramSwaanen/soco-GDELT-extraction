import pandas as pd
import random

df = pd.read_csv("Google_output_with_sentiment.csv")
df = df[~df.MainText.str.contains("vacuum")]

POSITIVE_CUTOFF = 0.5
NEGATIVE_CUTOFF = -0.5
SAMPLE_SIZE = 3

positive = df[df.Sentiment_Score > POSITIVE_CUTOFF]
negative = df[df.Sentiment_Score < NEGATIVE_CUTOFF]
neutral = df[df.Sentiment_Score < POSITIVE_CUTOFF]
neutral = neutral[neutral.Sentiment_Score > NEGATIVE_CUTOFF]

print("************NEXT RUN*************")
print("MANUAL EVALUATION POSITIVE:")
indices = random.sample(range(len(positive)),SAMPLE_SIZE)
for i in indices:
    datapoint = positive.iloc[i]
    print(str(i) + ":")
    print("Sentiment score: ", datapoint.Sentiment_Score)
    print("Main text:", datapoint.MainText) 
    print() 

print("MANUAL EVALUATION NEUTRAL:")
indices = random.sample(range(len(neutral)),SAMPLE_SIZE)
for i in indices:
    datapoint = neutral.iloc[i]
    print(str(i) + ":")
    print("Sentiment score: ", datapoint.Sentiment_Score)
    print("Main text:", datapoint.MainText) 
    print()  

print("MANUAL EVALUATION NEGATIVE:")
indices = random.sample(range(len(negative)),SAMPLE_SIZE)
for i in indices:
    datapoint = negative.iloc[i]
    print(str(i) + ":")
    print("Sentiment score: ", datapoint.Sentiment_Score)
    print("Main text:", datapoint.MainText) 
    print()  


