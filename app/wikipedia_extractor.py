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
        error_message = f"**Disambiguation Error** \n\n"
        error_message += f"The title '{article_title}' is ambiguous and can refer to multiple pages.😞\n\n"
        error_message += f"Please try to disambiguate the title by selecting one of the following options:\n\n"
        error_message += f"{e.options}\n"
        return Exception(error_message), None
    except wikipedia.exceptions.PageError:
        error_message = f"**Page Not Found**\n"
        error_message += f"The page '{article_title}' was not found on Wikipedia. 🤔\n"
        error_message += f"Please check the title and try again.\n"
        return Exception(error_message), None
