import requests
from bs4 import BeautifulSoup
import wikipedia
import datetime


def get_article_title_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1", class_="firstHeading").text
    return title


def extract_text_from_wikipedia(title_or_url):
    if title_or_url.startswith("https://"):
        article_title = get_article_title_from_url(title_or_url)
    else:
        article_title = title_or_url
    try:
        page = wikipedia.page(article_title)
        text = page.content
        return text, article_title
    except wikipedia.exceptions.DisambiguationError as e:
        raise ValueError(f"Disambiguation error: {e} 😞")
    except wikipedia.exceptions.PageError:
        raise ValueError(f"Page not found: {article_title} 🤔")
