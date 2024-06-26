import pandas as pd
from google.cloud import language_v2

#project id: soco-sentiment
#email address: b-swaanen@soco-sentiment.iam.gserviceaccount.com
#api key: AIzaSyAyJQ0WQfes4exIme4p3iMe1worF2B55t4

# Initialize the client for Google Natural Language API
client = language_v2.LanguageServiceClient()