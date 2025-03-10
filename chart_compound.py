import numpy as np
import matplotlib.pyplot as plt

# Execute the query and read into a pandas dataframe
df = result_table

# Convert the 'customer_feedback_timestamp' to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Group by month and calculate the mean sentiment score for each week
df_monthly = df.set_index("Timestamp").resample("M").mean()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df_monthly.index, df_monthly["COM"], marker='o', linestyle='-')
plt.title('Sentiment Score (Compound) Over Time (Monthly)')
plt.xlabel('Date')
plt.ylabel('Sentiment Score (Compound)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
