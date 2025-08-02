import streamlit as st
from hardware import extract_data_from_paragraph

st.set_page_config(page_title="Hardware Price Extractor", layout="centered")

st.title("🔍 Hardware Item Price Extractor")
st.markdown("Paste a paragraph describing hardware items (e.g., Door, Plywood) and their prices.")

paragraph = st.text_area("📝 Input Paragraph", height=250)

if st.button("Extract Data"):
    if not paragraph.strip():
        st.warning("Please enter a paragraph.")
    else:
        with st.spinner("Extracting data..."):
            result = extract_data_from_paragraph(paragraph)
        st.markdown("### 📊 Extracted Table")
        st.markdown(result)
