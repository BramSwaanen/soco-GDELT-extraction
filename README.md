# GDELT-extraction

The code in this repo can be used to extract information about relevant events from relevant newspapers in GDELT data files. This is can be done by editing newspaper_regex and ai_regex regular expressions in csv_saver.py to the newspaper and subject of your choosing and then running
1. python csv_saver.py to extract the contents of relevant articles;
2. python cut_data.py to reformat the article content strings for sentiment analysis;
3. python google_sentiment_analysis.py to have Google's api analyse the articles sentiment or python textlob  and then
4. python grapher.py to create the articles' monthly average's rolling average per newspaper.
