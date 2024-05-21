#libraries
import streamlit as st
from datetime import date
from pytrends.request import TrendReq
pytrends = TrendReq()

keywords = ["Python","R","C++","Java","HTML"]
pytrends.build_payload(keywords,timeframe="today 5-y")
df = pytrends.interest_over_time()
del df["isPartial"]

#Web Content
st.title("First Streamlit Web Page")
st.write("Web page text add for do")


##input
name = st.text_input("please enter username : ")
password = st.text_input("please enter password : ",type="password")

#birthday_date = st.date_input("please enter birthday date : ", min_value=date(1900,1,1))
st.button("login")

#st.camera_input("Upload Image")

st.video("https://youtu.be/09XGap8QiL8?feature=shared")

add_selectbox = st.sidebar.selectbox("How would you like to be contac ?",("E-mail","Phone"))


st.dataframe(df,use_container_width=True)