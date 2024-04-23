import streamlit as st
from wikipedia_extractor import extract_text_from_wikipedia
from summarizer import summarize_text


def main():
    st.title("Wikipedia Text Extractor and Summarizer 📚")
    st.write("----------------------------")

    choice = st.selectbox(
        "Choose an option:", ["Enter a topic title", "Enter a Wikipedia page URL"]
    )

    if choice == "Enter a topic title":
        title = st.text_input(
            "Enter a topic title:", placeholder="e.g. Artificial Intelligence"
        )
        if st.button("Extract Text 📄"):
            text, article_title = extract_text_from_wikipedia(title)
            if text:
                st.write(
                    f"Text extracted from Wikipedia article: **{article_title}** 📄"
                )
                st.write(text)
                summary = summarize_text(text)
                st.write("Summary:")
                st.write(summary)
    elif choice == "Enter a Wikipedia page URL":
        url = st.text_input(
            "Enter a Wikipedia page URL:",
            placeholder="e.g. https://en.wikipedia.org/wiki/Artificial_Intelligence",
        )
        if st.button("Extract Text 📄"):
            text, article_title = extract_text_from_wikipedia(url)
            if text:
                st.write(
                    f"Text extracted from Wikipedia article: **{article_title}** 📄"
                )
                st.write(text)
                summary = summarize_text(text)
                st.write(
                    """<h1 style="color:blue; font-size:40px;">"Summary"</h1>""",
                    unsafe_allow_html=True,
                )
                st.write(summary)


if __name__ == "__main__":
    main()
