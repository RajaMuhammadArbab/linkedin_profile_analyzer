import language_tool_python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import openai
from django.conf import settings

tool = language_tool_python.LanguageTool('en-US')
vader = SentimentIntensityAnalyzer()

def analyze_grammar(text):
    matches = tool.check(text)
    return tool.correct(text), matches

def analyze_sentiment(text):
    blob = TextBlob(text)
    vader_score = vader.polarity_scores(text)
    return blob.sentiment, vader_score

def get_openai_suggestion(text, api_key):
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a LinkedIn profile expert."},
            {"role": "user", "content": f"Analyze this profile section and give suggestions: {text}"}
        ]
    )

    return response.choices[0].message.content
