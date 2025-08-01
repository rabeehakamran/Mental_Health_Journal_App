from textblob import TextBlob
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# List of common mental health keywords
MENTAL_HEALTH_TERMS = [
    "anxiety", "depression", "lonely", "worthless", "overwhelmed",
    "burnout", "panic", "sad", "angry", "hopeless", "tired", "stress",
    "fear", "scared", "crying", "numb", "pressure", "broken"
]

def analyze_journal(text):
    # Sentiment Analysis with TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "positive"
    elif polarity < -0.2:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Keyword Extraction with spaCy
    doc = nlp(text.lower())
    found_keywords = []

    for token in doc:
        if token.text in MENTAL_HEALTH_TERMS and token.text not in found_keywords:
            found_keywords.append(token.text)

    return {
        "sentiment": sentiment,
        "keywords": found_keywords
    }
