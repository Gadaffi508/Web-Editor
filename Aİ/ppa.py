#->Use your API keys securely. Do not share them or embed them in code the public can view.
#-----------------------------------------------------------------------------------------
#AIzaSyA5OvwsFkWG-u4B91yE6EoYbwu_GsXAEYo

#-> import streamlit
import streamlit as st
#-----------------------------------------------------------------------------------------

#-> import google generativeai
import google.generativeai as geneia
#-----------------------------------------------------------------------------------------

#-> Image for read import library
import PIL as IMAGE
#-----------------------------------------------------------------------------------------

#-> API definition
geneia.configure(api_key = "AIzaSyA5OvwsFkWG-u4B91yE6EoYbwu_GsXAEYo")
#-----------------------------------------------------------------------------------------

#-> Create Title area
st.title("Gemini with Image Read")
#-----------------------------------------------------------------------------------------

#-> Set gemini version
model = geneia.GenerativeModel("gemini-pro-vision")
#-----------------------------------------------------------------------------------------

#-> Set ımage upload and image variable
image = st.file_uploader("Image upload",type=["jpg","png","jpeg","pdf"])
#-----------------------------------------------------------------------------------------

#-> Control image not null if
if image is not None:
#-----------------------------------------------------------------------------------------

    #-> image open and get image
    img = IMAGE.open(image)
    #-------------------------------------------------------------------------------------

    #-> Show in image
    st.image(img)
    #-------------------------------------------------------------------------------------

#-> Question text Title
Question = st.text_input("Question")
#-----------------------------------------------------------------------------------------

#-> Create button name ques
if st.button("Ques"):
#-----------------------------------------------------------------------------------------

    #-> create answer varibale and this ai answer
    answer = model.generate_content([Question,img],stream=True)
    #-------------------------------------------------------------------------------------

    #-> answer image read
    answer.resolve()
    #-------------------------------------------------------------------------------------

    #-> Show in Answer text
    st.write(answer.text)
    #-------------------------------------------------------------------------------------