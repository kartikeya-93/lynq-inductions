import streamlit as st
from pypdf import PdfReader

st.title("📄 Simple PDF Reader")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    reader = PdfReader(pdf_file)
    st.write(f"Total pages: {len(reader.pages)}")

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    st.text_area("Extracted text", text[:2000] + "...", height=300)

    query = st.text_input("Ask a question (keyword search)")
    if query:
        matches = [p.extract_text() for p in reader.pages if query.lower() in (p.extract_text() or "").lower()]
        if matches:
            st.write(f"Found {len(matches)} page(s) with '{query}':")
            for i, m in enumerate(matches, 1):
                st.write(f"--- Page {i} ---")
                st.write(m[:500] + "...")
        else:
            st.write("No matches found.")