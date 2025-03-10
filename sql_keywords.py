# Convert input string to a list of keywords, stripping any extra whitespace
keywords = [kw.strip() for kw in input_keywords.split(",")]

# Construct the SQL condition
sql_keywords = " OR ".join([f"customer_feedback LIKE '%{kw}%'" for kw in keywords])

print(sql_keywords)
