# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Apply the sentiment analysis to the 'CUSTOMER_FEEDBACK' column and create new columns for scores
df["compound"] = df["CUSTOMER_FEEDBACK"].apply(
    lambda sentence: sid.polarity_scores(sentence)["compound"]
)
df["neg"] = df["CUSTOMER_FEEDBACK"].apply(
    lambda sentence: sid.polarity_scores(sentence)["neg"]
)
df["neu"] = df["CUSTOMER_FEEDBACK"].apply(
    lambda sentence: sid.polarity_scores(sentence)["neu"]
)
df["pos"] = df["CUSTOMER_FEEDBACK"].apply(
    lambda sentence: sid.polarity_scores(sentence)["pos"]
)

# Display results in a table
result_table = pd.DataFrame(
    {
        "Sentence": df["CUSTOMER_FEEDBACK"],
        "COM": df["compound"],
        "NEG": df["neg"],
        "NEU": df["neu"],
        "POS": df["pos"],
        "Timestamp": df["CUSTOMER_FEEDBACK_TIMESTAMP"]
    }
)

# Display the table
print(result_table)
