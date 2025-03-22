import streamlit as st
from gemini_api import process_with_gemini


st.set_page_config(page_title="LL(1) Parser", layout="wide")

st.title("LL(1) Parser with Interactive Parse Trees & Downloadable Reports")

st.markdown("""
This application analyzes Context-Free Grammar (CFG), removes left recursion, applies left factoring, computes First & Follow sets, generates parsing tables, and provides step-by-step LL(1) parsing explanations.  
**New Features:**  
✔️ **Interactive Parse Trees**  
✔️ **Downloadable Reports (PDF)**
""")

grammar_input = st.text_area("Enter Grammar (each rule in a new line, e.g., `S -> A a | b`):", height=200)
input_string = st.text_input("Enter input string for parsing:")

if st.button("Process Grammar"):
    if not grammar_input.strip():
        st.warning("Please enter a valid grammar.")
    else:
        st.session_state['grammar'] = grammar_input
        result, parse_tree = process_with_gemini(grammar_input, input_string)

        st.subheader("Step-by-Step Processing")
        st.write(result)

        if parse_tree:
            st.subheader("Interactive Parse Tree")
            st.image(parse_tree, caption="Generated Parse Tree",  use_container_width=True)

       