import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load CSV file
df = pd.read_csv('outpu_cat_data.csv')

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment for each article
df['TextBlob_Sentiment'] = df['MainText'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['VADER_Sentiment'] = df['MainText'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Display results
print(df[['Headline', 'TextBlob_Sentiment', 'VADER_Sentiment']])

# Optionally save the DataFrame with sentiment analysis results
df.to_csv('sentiment_by_textlob_no_robots.csv', index=False)
