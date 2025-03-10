This repo captures a [Hex](https://app.hex.tech) notebook that I made and use regularly as a PM. There will be some Hex specific jank that I'll eventually fix.

### Files Recap
- raw_feedback.sql: SQL file containing the structure for the feedback table.
- inputs_example.py: Example script demonstrating input handling.
- sql_keywords.py: Script to handle SQL keyword operations.
- pre_process_text.py: Module for text preprocessing.
- sentiment_analysis.py: Main script to perform sentiment analysis.
- categorise_sentiment.py: Module to categorise sentiments.
- chart_compound.py: Script to generate sentiment charts.
- display_sentiment_ratio.md: Markdown file explaining sentiment ratio display.

# sentiment-analysis Features
### Inputs
This tool will take 3 inputs from the user:
1. Keywords / raw feedback
2. Start Date
3. End Date

Then it will fetch raw feedback from the customer feedback table. This table is populated by player feedback through UI's like:

The raw feedback is then displayed and available for download. That allows you to check that you're pulling the kind of feedback you want to see.

### Pre-processing Text
Then the tool will prepare the feedback to be better understood by some preprocessing techniques. Specifically we:
- Tokenise the text (e.g.: 'Do not send me any freaking email' -> 'Do', 'not', 'send', 'me', 'any', 'freaking', 'email')
- Remove stop words (e.g.: 'Do', 'not', 'send', 'me', 'any', 'freaking', 'email' -> 'send', 'freaking', 'email')
- Lemmatize the tokens (e.g.: 'freaking' -> 'freak')
- Join it all back up into a single string for sentiment analysis ('send freak email')

### Sentiment Analysis Scores
With the processed strings, the tool then uses NLTK Sentiment Analyzer to score each piece of feedback with four scores:
1. Compound Score (-1 -> 1) - consider this an aggregate score of the other three scores. -1 is very negative, 0 is very neutral, 1 is very positive)
2. Negative Score (0 -> 1)
3. Neutral Score (0 -> 1)
4. Positive Score (0 -> 1)

### Interpreting Analysis
Once each feedback is scored, the tool charts the compound scores grouped by calendar month. Then a Sentiment Ratio is calculated.
Quick Sentiment Ratio guide from GPT:
- Greater than 1 (>1) → More Positive Sentiment
    - Example: Sentiment Ratio = 3
    - This means positive sentiment is 3x higher than negative sentiment. 
    - Your users/customers are generally happy.

- Close to 1 (~1) → Balanced Sentiment
    - Example: Sentiment Ratio = 1.1
    - This means there are about as many positive comments as negative ones. 
    - Mixed sentiment, indicating neutral or polarized feedback.

- Less than 1 (<1) → More Negative Sentiment
    - Example: Sentiment Ratio = 0.5
    - This means negative sentiment is twice as high as positive sentiment.
    - Users are unhappy, and you may need to investigate why.
    
- Near Zero (~0) → Overwhelmingly Negative Sentiment
    - Example: Sentiment Ratio = 0.1
    - This means negative sentiment is 10x higher than positive sentiment.
    - Likely indicates serious dissatisfaction or frustration.
