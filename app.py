import streamlit as st
from gemini_api import process_with_gemini


st.set_page_config(page_title="LL(1) Parser", layout="wide")

# Create two columns: one for the image and one for the title
col1, col2 = st.columns([5,7])  # You can adjust the proportions as needed

# Add the logo image in the first column
with col1:
    logo_path = 'balakrishna_sir.jpg'  # Local path or URL to your logo
    st.image(logo_path, width=400)  # Adjust width as necessary

# Add the title text in the second column
with col2:
    st.title("LL(1) Parser with Interactive Parse Trees")
    st.markdown("""
This application analyzes Context-Free Grammar (CFG), removes left recursion, applies left factoring, computes First & Follow sets, generates parsing tables, and provides step-by-step LL(1) parsing explanations.  
**New Features:**  
✔️ **Interactive Parse Trees**  
✔️ **Different types of error recovery** 
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

    st.title('Under the guidance of "Dr N.Bala Krishna Sir"')
