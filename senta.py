import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores['compound'] 
def main():
    # 加载 CSV 文件
    file_path = 'outpu_cut_data.csv'  # 请将此路径替换为您文件的实际路径
    data = pd.read_csv(file_path)

    # 对 'MainText' 列应用情感分析
    data['Sentiment'] = data['MainText'].apply(analyze_sentiment)

    # 保存结果到新的 CSV 文件
    output_file_path = 'sentiment_analysis_results.csv'  # 您可以自定义输出文件的路径和文件名
    data.to_csv(path_or_buf=output_file_path, index=False)


    print("情感分析完成，结果已保存到：", output_file_path)

if __name__ == "__main__":
    main()
