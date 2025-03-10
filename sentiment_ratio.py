sentiment_ratio = df["POS"].sum() / (
    df["NEG"].sum() + 1
)  # +1 to avoid division by zero
