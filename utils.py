import random
from textblob import TextBlob

# --------------------
# Sentiment Analysis
# --------------------
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment


# --------------------
# Keyword Detection
# --------------------
def detect_keywords(text):
    keywords_list = [
        "stress", "tired", "burnout", "anxiety", "hopeless", "angry", "lonely",
        "peace", "grateful", "productive", "happy", "calm", "panic", "overwhelmed",
        "motivated", "discouraged", "exhausted", "rest", "focus", "self-doubt"
    ]

    found_keywords = []

    lower_text = text.lower()

    for word in keywords_list:
        if word in lower_text:
            found_keywords.append(word)

    return found_keywords


# --------------------
# Quote Suggestion
# --------------------
SENTIMENT_QUOTES = {
    "positive": [
        "You're doing amazing — don't stop now!",
        "Positive mind. Positive vibes. Positive life.",
        "Celebrate your small wins, they matter too!"
    ],
    "neutral": [
        "Some days are just okay — and that’s okay.",
        "Balance is better than perfection.",
        "You’re allowed to pause and just be."
    ],
    "negative": [
        "You’re stronger than you think.",
        "Even the darkest night will end and the sun will rise.",
        "It’s okay not to be okay — just don’t give up."
    ]
}

KEYWORD_QUOTES = {
    "burnout": [
        "Rest isn’t a reward — it’s a requirement.",
        "Burnout is not a badge of honor. Slow down.",
        "Your worth isn’t measured by productivity."
    ],
    "stress": [
        "One thing at a time. Breathe.",
        "Your peace matters more than perfection.",
        "It’s okay to slow down."
    ],
    "tired": [
        "Rest. You’re not a machine.",
        "It’s okay to take a step back when you need it.",
        "You deserve rest as much as work."
    ],
    "anxiety": [
        "You don’t have to control everything.",
        "Your worries are valid, but so is your strength.",
        "This too shall pass. Breathe."
    ],
    "hopeless": [
        "There is always hope, even when you can't feel it.",
        "Hold on — your breakthrough might be tomorrow.",
        "Don’t confuse a bad moment with a bad life."
    ],
    "angry": [
        "Anger is a valid emotion — feel it, then let it go.",
        "You’re not your anger. You’re your calm too."
    ],
    "lonely": [
        "You are not alone. Even when it feels like it.",
        "Someone out there is thankful you exist.",
        "Reach out — even a small connection helps."
    ],
    "peace": [
        "Protect your peace. Always.",
        "Peace is not the absence of chaos, but presence of calm."
    ],
    "grateful": [
        "Gratitude turns what we have into enough.",
        "The more you’re grateful, the more you attract blessings."
    ],
    "productive": [
        "Progress, not perfection.",
        "Your discipline today becomes freedom tomorrow."
    ],
    "happy": [
        "Let joy be your strength.",
        "Happiness is found in little moments. Hold on to them."
    ],
    "calm": [
        "Stay calm — you’re in control.",
        "You can handle this, peacefully and powerfully."
    ],
    "panic": [
        "Take deep breaths. You are safe.",
        "This moment will pass. You are okay."
    ],
    "overwhelmed": [
        "Break it down. One thing at a time.",
        "You don’t have to carry everything at once."
    ],
    "motivated": [
        "You’re on fire — keep the momentum going!",
        "You’re closer than you think. Keep pushing."
    ],
    "discouraged": [
        "It’s okay to start over — you’re not behind.",
        "Every setback is a setup for a comeback."
    ],
    "exhausted": [
        "Your body is whispering — listen and rest.",
        "Being tired isn’t weakness — it’s a signal."
    ],
    "rest": [
        "Rest is productive.",
        "Silence and stillness are powerful tools."
    ],
    "focus": [
        "Cut out the noise. Focus is freedom.",
        "You have everything you need to get this done."
    ],
    "self-doubt": [
        "You’ve made it through 100% of your worst days.",
        "You are more capable than you believe."
    ]
}


def get_quote(sentiment, keywords=[]):
    matching_quotes = []

    for kw in keywords:
        if kw in KEYWORD_QUOTES:
            matching_quotes.extend(KEYWORD_QUOTES[kw])

    if matching_quotes:
        return random.choice(matching_quotes)
    elif sentiment in SENTIMENT_QUOTES:
        return random.choice(SENTIMENT_QUOTES[sentiment])
    else:
        return "Keep going — your story isn’t over yet."


# --------------------
# Final Combined Analysis Function
# --------------------
def analyze_journal_entry(text):
    sentiment = analyze_sentiment(text)
    keywords = detect_keywords(text)
    return {
        "sentiment": sentiment,
        "keywords": keywords
    }
