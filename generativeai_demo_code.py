
import google.generativeai as palm
import streamlit as st
import generativeai_demo_code as gdmc


st.title("Google's PALM 2")
palm.configure(api_key="API_KEY")
text_search = st.text_input("What would you like to have summarized?", value="")


defaults = {
  'model': 'models/text-bison-001',
  'temperature': 1,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
prompt = f"""Summarize this paragraph and detail some relevant context.

Text={text_search}

Summary:
"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
st.write(response.result) 