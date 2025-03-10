def categorize_sentiment(COM):
    if COM >= 0.2:
        return "Positive"
    elif COM <= -0.2:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment_Category"] = df["COM"].apply(categorize_sentiment)
