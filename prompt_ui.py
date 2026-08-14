from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")   this is static prompthing where user types the whole prompt themselves 

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

template = load_prompt('template.json')

#fill the placeholder
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content[0]['text'])


# here chianing technique is being used where we call invoke only one time not two times like earlier
if st.button("Summarize"):
    chain = template | model
    result = chain.invoke(
        {
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        }
    )
    st.write(result.content[0]['text'])