import pandas as pd
from google.cloud import language_v2

def analyze_sentiment_in_csv(csv_file: str, output_csv: str) -> None:
    """
    Reads content from a CSV file, analyzes sentiment of text using Google Natural Language API, and saves results with the original data.

    Args:
      csv_file: Path to the input CSV file containing the text to analyze.
      output_target: Path to the output CSV file to save sentiment analysis results merged with the original data.
    """
    # Load data
    df = pd.read_csv(csv_file) 
    
    # Initialize the client for Google Natural Language API
    client = language_v2.LanguageServiceClient()

    # Analyze sentiment for each row and append results
    sentiment_scores = []
    sentiment_magnitudes = []
    for i,text_content in enumerate(df['MainText']):  # Assumes 'MainText' column has the text content
        print(f"Text {i} of {len(df['MainText'])}")
        document = {
            "content": text_content,
            "type_": language_v2.Document.Type.PLAIN_TEXT,
            "language_code": "en",
        }
        encoding_type = language_v2.EncodingType.UTF8
        response = client.analyze_sentiment(
            request={"document": document, "encoding_type": encoding_type}
        )
        
        # Collect sentiment scores and magnitudes
        document_sentiment = response.document_sentiment
        sentiment_scores.append(document_sentiment.score)
        sentiment_magnitudes.append(document_sentiment.magnitude)

    # Append sentiment analysis to the dataframe
    df['Sentiment_Score'] = sentiment_scores
    df['Sentiment_Magnitude'] = sentiment_magnitudes

    # Save the updated DataFrame to a new CSV
    df.to_csv(output_csv, index=False)

    print(f"Sentiment analysis completed. Results saved to {output_csv}")

# Example usage
analyze_sentiment_in_csv('more_dates_outpu_cat_data.csv', 'more_dates_Google_output_with_sentiment_no_robots.csv')
