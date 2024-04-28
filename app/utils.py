from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
import spacy


def write_word_cloud(text):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt


def sentement_report(text):
    sentiment = TextBlob(text).sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    report = (
        f"**Sentiment:** {sentiment_label}\n"
        f"**Polarity:** {polarity:.2f} (How positive or negative the text is)\n"
        f"**Subjectivity:** {subjectivity:.2f} (How subjective or opinion-based the text is)\n"
    )
    if polarity > 0:
        polarity_message = "The sentiment of the text is **positive**, indicating that the text expresses a favorable opinion or emotion."
    elif polarity < 0:
        polarity_message = "The sentiment of the text is **negative**, indicating that the text expresses an unfavorable opinion or emotion."
    else:
        polarity_message = "The sentiment of the text is **neutral**, indicating that the text does not express a strong opinion or emotion."

    return report, polarity_message


def get_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    unique_entities = list(set(entities))  # Remove duplicates
    return unique_entities
