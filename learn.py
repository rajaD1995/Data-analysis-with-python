import streamlit as st
import time as t
#display image
st.image("315952201_1259716428155294_170271717689739812_n (1).jpg")

st.title("Hello World! : title") #title
st.header("Machine larning: header") #header4
st.subheader("Linear Regression: subheader")
st.info("Here is the info of Raja: info") #information
st.warning("come on time 👀: warning") #warnings
st.error("Wrong password: error") #to show error

def name(a=5,b=3):
    return a+b
#you can not wite a iterable function in stramlit. return is must
# def name1():
#     k = 'raja'
#     for i in k:
#         print(i)
# st.write(name1())

user_name = name()
st.write(f"Here is the sum: {name()}: write") #we can use function directly in write.
st.write(range(50))  #it will print as code --- range(0, 50)
st.text(f"{user_name}: text")
st.text("Sum is completed: text")  #adding variable in text.
st.success("Congrats: success")
st.subheader("markdown with nothing,#, ##, ###")
st.markdown("Raja") #normal size 
st.markdown("# Raja") #size is max 
st.markdown("## Raja")  #size getting little smaller
st.markdown("### Raja") #size getting more small
st.markdown(":moon:") #emoji of moon
st.caption("Here is the caption")

#math expression
st.latex(r''' a+b x^6 +c''')


#widget
st.checkbox("Login")
st.button("Click to save it")
st.radio("Pick your gender",["male","Female","other"])
st.selectbox("Select your course",["None","ML","Cloud","Gen AI","Data Science"])
st.multiselect("Select your course",["Other","ML","Cloud","Gen AI","Data Science"])
st.select_slider("select select_slider",[i for i in range(0,51)])
st.select_slider("select select_slider",["good","very good","Excelent"])

#slider
st.slider("Select a number from slider",0,30)

#select a number
st.number_input("number_input",0,30)

#text_input: Like asking for email address
st.text_input("text_input: email address")

#date_input
st.date_input("date_input:")

#time_input
st.time_input("time_input: ")

#text_area: Like 150 letters of description
st.text_area("Enter your throught wihtin 150 words",max_chars=150)

#file uploder
st.file_uploader("file_uploader: ")

st.color_picker("color_picker: ")

#teack_progress
st.progress(90)  #display 90% of progress has been done.

#spinner. Excution time legging sign or loading sign.
with st.spinner("Loading_spinner..."):
    t.sleep(2)  #for 2 sec loading sign will appear

#ballon_will_appear on the screen
st.balloons()

#you want to diplay something left side of the screen
st.sidebar.title("Welcome to my page")
st.sidebar.text_input("Enter your email: ")
st.sidebar.text_input("Enter your password: ")
st.sidebar.button("submit")
st.sidebar.radio("Professional exprt",["Amature","student","expert"])


#data_visualisation

import pandas as pd
import numpy as np
import random
st.title("Bar chart")
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data=data)
st.title("Line chart")
st.line_chart(data)
st.title("Area chart")
st.area_chart(data)