import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates


file_path = "Google_output_with_sentiment.csv"  
data = pd.read_csv(file_path)

# Get 'Month' and 'Year' columns
data.insert(0,'Month',[int(str(i)[:6]) for i in data.Date])
data.insert(0,'Year',[int(str(i)[:4]) for i in data.Date])
print(data.head())

# Convert date columns to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data['Month'] = pd.to_datetime(data['Month'], format='%Y%m')
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

print(data.head())

# Group by Date and NewsPaper and calculate mean of Sentiment_Score
grouped_data = data.groupby(['Month', 'NewsPaper'])['Sentiment_Score'].mean().unstack()

# Plotting
plt.figure(figsize=(14, 7))
sns.lineplot(data=grouped_data, dashes=False)
plt.title('Average Sentiment Score Over Time by Newspaper')
plt.ylabel('Average Sentiment Score')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.legend(title='Newspaper', title_fontsize='13', fontsize='11', loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
