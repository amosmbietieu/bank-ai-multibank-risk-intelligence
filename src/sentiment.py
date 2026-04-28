from textblob import TextBlob

def sentiment_score(text):
    """
    Returns polarity score.
    """
    blob = TextBlob(text)
    return round(blob.sentiment.polarity, 3)
