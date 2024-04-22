import requests
from bs4 import BeautifulSoup
import wikipedia


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
        print(f"Disambiguation error: {e}")
        return None
    except wikipedia.exceptions.PageError:
        print(f"Page not found: {article_title}")
        return None


def save_as_txt_file(text, title):
    with open(f"{title}.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("Extracted text has been saved to 'extracted_text.txt'")


def main():
    print("Wikipedia Text Extractor")
    print("----------------------------")
    print("1. Enter a topic title")
    print("2. Enter a Wikipedia page URL")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter a topic title: ")
        text, article_title = extract_text_from_wikipedia(title)
    elif choice == "2":
        url = input("Enter a Wikipedia page URL: ")
        text, article_title = extract_text_from_wikipedia(url)
    else:
        print("Invalid choice. Exiting.")
        return

    if text:
        print(f"Text extracted from Wikipedia article: {article_title}")
        print(text)
        save = input("Do you want to save the extracted text to a file? (y/n): ")
        if save.lower() == "y":
            save_as_txt_file(text, article_title)


if __name__ == "__main__":
    main()
