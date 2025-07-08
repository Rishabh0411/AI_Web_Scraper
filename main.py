import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content,
)
from parse import parse_with_ollama

st.title("AI Web Scraper")

url = st.text_input("Enter a Website URL (include http:// or https://):", key="url_input")

if st.button("Scrape Site", key="scrape_button"):
    if not url.startswith(("http://", "https://")):
        st.error("Please enter a valid URL with http:// or https://")
    else:
        st.write("Scraping.....")
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300, key="dom_content_area")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Please provide a prompt....", key="prompt_input")

    if st.button("Parse", key="parse_button"):
        st.write("Parsing.....")
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parse_description)
        st.write(result)
