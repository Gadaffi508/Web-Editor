#->Use your API keys securely. Do not share them or embed them in code the public can view.
#-----------------------------------------------------------------------------------------
#AIzaSyA5OvwsFkWG-u4B91yE6EoYbwu_GsXAEYo

#-> import streamlit
import streamlit as st
#-----------------------------------------------------------------------------------------

#-> import google generativeai
import google.generativeai as geneia
#-----------------------------------------------------------------------------------------

#-> API definition
geneia.configure(api_key = "AIzaSyA5OvwsFkWG-u4B91yE6EoYbwu_GsXAEYo")
#-----------------------------------------------------------------------------------------

#-> Create Title area
st.title("Gemini with let's talk")
#-----------------------------------------------------------------------------------------

#-> Set gemini version
model = geneia.GenerativeModel("gemini-1.5-pro-latest")
#-----------------------------------------------------------------------------------------

#-> Question Memeory
chat = model.start_chat(history=[])
#-----------------------------------------------------------------------------------------

#-> Question text Title
Question =st.text_input("Enter question")
#-----------------------------------------------------------------------------------------

answer = ""

#-> Create button for question enter later answer see
if st.button("Question"):
#-----------------------------------------------------------------------------------------

    #-> Post the answer
    answer = chat.send_message(Question)
    #-------------------------------------------------------------------------------------

    #-> show in text
    st.write(answer.text)
    #-------------------------------------------------------------------------------------

#-> Add history ai
chat.history.append(answer)
#-------------------------------------------------------------------------------------

#-> Write history text
st.write(chat.history)
#-------------------------------------------------------------------------------------