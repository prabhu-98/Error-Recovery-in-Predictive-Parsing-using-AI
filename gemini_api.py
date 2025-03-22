import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from environment file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

def process_with_gemini(grammar, input_string):
    prompt = f"""
    I need a complete step-by-step analysis of a grammar and parsing of an input string. Please maintain consistent formatting throughout your response and provide ALL requested outputs.

    ## INPUT DATA:
    Grammar: f{grammar}
    Input string to parse: {input_string}

    ## REQUIRED ANALYSIS STEPS AND OUTPUTS:

    1. Context-Free Grammar Verification
    - Analyze if the given grammar is a Context-Free Grammar (CFG)
    - Show your reasoning with specific criteria for CFG verification
    - Provide a clear YES/NO conclusion

     2. Grammar Transformation (if needed)
    - If NOT a CFG or if the grammar has left recursion or needs left factoring:
    * Show the step-by-step elimination of left recursion
    * Show the step-by-step application of left factoring
    * Present the final transformed grammar
    - If no transformation needed, explicitly state this

    3. First and Follow Sets
    - Compute the FIRST set for each non-terminal (show calculation steps)
    - Compute the FOLLOW set for each non-terminal (show calculation steps)
    - Present both sets in clearly formatted tables

    4. LL(1) Parsing Table Construction
    - Construct the complete LL(1) parsing table
    - Show the application of parsing table rules step-by-step
    - Format the table clearly with non-terminals as rows and terminals as columns
    - Indicate any conflicts (if they exist) and what they mean for the grammar

    5. Visual Parse Tree
    - Generate a visual representation of the parse tree for the given grammer
    - Use ASCII art for clear visualization with proper indentation and structure
    - Format it so it can be easily converted to an image

    6. Step-by-Step Parsing Process
    - Show EACH step of the parsing process using the LL(1) parsing table
    - For each step include:
    * Current stack contents
    * Remaining input
    * Action taken (match, expand, error)
    * Rule applied (if any)
    - Provide clear explanations for each parsing decision
    - Indicate whether the string is accepted or rejected by the grammar

    VALIDATION AND CONCLUSION
    - Confirm whether the input string is valid according to the grammar
    - Summarize key insights about the grammar (LL(1) status, any special properties)
    """
    # Generate response using Gemini API
    response = model.generate_content(prompt)

    # Extract parse tree separately if provided
    response_text = response.text if response.text else "No response received."
    
    if "Parse Tree Representation:" in response_text:
        result_text, parse_tree = response_text.split("Parse Tree Representation:", 1)
        return result_text.strip(), parse_tree.strip()
    
    return response_text.strip(), None
