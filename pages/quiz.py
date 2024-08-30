

import streamlit as st
def chatbot(question):
    from openai import OpenAI

    client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 안동의 명물인지 아닌지 알려주는 봇이야. 맞다면 y로 아니면, n으로 대답해줘"},
        {"role": "user", "content": question}
    ]
    )
    return completion.choices[0].message.content


q="안동에서 유명한것"

ans=st.text_input(q)
if st.button("정답 확인하기"):
    #챗지피티가 answer가 맞는지 학인 후 
    result=chatbot(ans)
    #정답 여부 return
    if result=='y':
        st.write("정답")
    else:
        st.write("오답")
'''
# Title of the app
st.title("3-Choice Question Example")

# Question
st.write("What is the capital of France?")

# Options
options = ["Berlin", "Madrid", "Paris"]

# Create a radio button for the options
choice = st.radio("Choose your answer:", options)

# Button to submit the answer
if st.button("Submit"):
    if choice == "Paris":
        st.success("Correct! Paris is the capital of France.")
    else:
        st.error("Incorrect. The correct answer is Paris.")
'''