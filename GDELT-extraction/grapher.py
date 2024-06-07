import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = "Google_output_with_sentiment.csv"  
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# Group by Date and NewsPaper and calculate mean of Sentiment_Score
grouped_data = data.groupby(['Date', 'NewsPaper'])['Sentiment_Score'].mean().unstack()

# Plotting
plt.figure(figsize=(14, 7))
sns.lineplot(data=grouped_data, dashes=False)
plt.title('Average Sentiment Score Over Time by Newspaper')
plt.ylabel('Average Sentiment Score')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend(title='Newspaper', title_fontsize='13', fontsize='11', loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()