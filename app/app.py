import streamlit as st
from wikipedia_extractor import *
from utils import *
from summarizer import summarize_text


def main():
    st.title("Wikipedia Text Extractor and Summarizer 📚")
    st.write("----------------------------")

    st.sidebar.header("Customize Your Experience")
    st.sidebar.write("----------------------")

    choice = st.selectbox(
        "Choose an option:", ["Enter a topic title", "Enter a Wikipedia page URL"]
    )
    st.sidebar.write("Customize Your Analysis:")
    sentiment_analysis = st.sidebar.checkbox("Sentiment Analysis", value=False)
    entity_recognition = st.sidebar.checkbox("Entity Recognition", value=False)

    if choice == "Enter a topic title":
        title = st.text_input(
            "Enter a topic title:", placeholder="e.g. Artificial Intelligence"
        )
        if st.button("Let's dig deeper 📄"):
            text, article_title = extract_text_from_wikipedia(title)
            if isinstance(text, str):

                st.write(
                    f"Text extracted from Wikipedia article: **{article_title.strip()}** 📄"
                )

                plt = write_word_cloud(text)
                st.pyplot(plt)

                summary = summarize_text(text)
                st.write(
                    """<h1 style="color:#399685; font-size:20px;">Summary</h1>""",
                    unsafe_allow_html=True,
                )
                st.write(summary)

                if sentiment_analysis:
                    st.divider()
                    st.write(
                        """<h1 style="color:#9f0fbc; font-size:20px;">Sentiment Analysis:</h1>""",
                        unsafe_allow_html=True,
                    )

                    report, polarity_message = sentement_report(text)

                    st.write(report)
                    st.write(polarity_message)

                if entity_recognition:
                    st.divider()
                    st.write(
                        """<h1 style="color:#9f0fbc; font-size:20px;">Entity Recognition:</h1>""",
                        unsafe_allow_html=True,
                    )

                    unique_entities = get_entities(text)
                    if unique_entities:
                        st.write("**Entities found:**")
                        entity_table = []
                        for entity in unique_entities:
                            entity_table.append(
                                {"Entity": entity[0], "Label": entity[1]}
                            )
                        st.table(entity_table)
                    else:
                        st.write("**No entities were found in the text.**")
            else:
                st.error(str(text), icon="🚨")
    elif choice == "Enter a Wikipedia page URL":
        url = st.text_input(
            "Enter a Wikipedia page URL:",
            placeholder="e.g. https://en.wikipedia.org/wiki/Artificial_Intelligence",
        )
        if st.button("Let's dig deeper 📄"):
            text, article_title = extract_text_from_wikipedia(url)
            if isinstance(text, str):
                st.write(
                    f"Text extracted from Wikipedia article: **{article_title.strip()}** 📄"
                )

                plt = write_word_cloud(text)
                st.pyplot(plt)

                summary = summarize_text(text)
                st.write(
                    """<h1 style="color:#399685; font-size:20px;">Summary</h1>""",
                    unsafe_allow_html=True,
                )
                st.write(summary)

                if sentiment_analysis:
                    st.divider()
                    st.write(
                        """<h1 style="color:#9f0fbc; font-size:20px;">Sentiment Analysis:</h1>""",
                        unsafe_allow_html=True,
                    )

                    report, polarity_message = sentement_report(text)

                    st.write(report)
                    st.write("")
                    st.write(polarity_message)

                if entity_recognition:
                    st.divider()
                    st.write(
                        """<h1 style="color:#9f0fbc; font-size:20px;">Entity Recognition:</h1>""",
                        unsafe_allow_html=True,
                    )
                    unique_entities = get_entities(text)
                    if unique_entities:
                        st.write("**Entities found:**")
                        entity_table = []
                        for entity in unique_entities:
                            entity_table.append(
                                {"Entity": entity[0], "Label": entity[1]}
                            )
                        st.table(entity_table)
                    else:
                        st.write("**No entities were found in the text.**")
            else:
                st.error(str(text), icon="🚨")


if __name__ == "__main__":
    main()
