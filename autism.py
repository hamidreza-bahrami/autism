import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
x = data['x']

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل تشخیص اوتیسم خفیف در کودکان</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>علائم فرزند خود را وارد کنید</h2>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>True = بله , False = خیر</h4>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    st.write("<h4 style='text-align: center; color: gray;'>:آیا کودک شما</h4>", unsafe_allow_html=True)

    calling = (True , False)
    calling = st.selectbox('به صدازدن نام پاسخ نمی دهد؟', calling)

    eye = (True , False)
    eye = st.selectbox('از تماس چشمی خودداری می کند؟', eye)

    simplegame	 = (True , False)
    simplegame	 = st.selectbox('بازی های تعاملی ساده مثل دالی موشه را انجام نمی دهد؟', simplegame)

    handy = (True , False)
    handy = st.selectbox('از حرکات دست کمتر استفاده می کند؟', handy)

    joyshare = (True , False)
    joyshare = st.selectbox('علایق خود را با دیگران به اشتراک نمی گذارد؟', joyshare)

    joyshow = (True , False)
    joyshow = st.selectbox('چیزی را که برایش جالب است به شما نشان نمی دهد؟', joyshow)

    recognize = (True , False)
    recognize = st.selectbox('متوجه علائم ناراحتی در چهره و رفتار دیگران نمی شود؟', recognize)

    otherkids = (True , False)
    otherkids = st.selectbox('به کودکان دیگر توجه نمی کند و با آن ها بازی نمی کند؟', otherkids)

    imagination = (True , False)
    imagination = st.selectbox('افکار و تخیلات خود را بروز نمی دهد؟', imagination)

    social = (True , False)
    social = st.selectbox('علاقه ای به برقراری ارتباط با دیگران ندارد؟', social)

    repeating = (True , False)
    repeating = st.selectbox('رفتارهای تکراری را بصورت افراطی و کلیشه ای انجام می هد؟', repeating)

    feeling = (True , False)
    feeling = st.selectbox('از نظر احساسی تحریک پذیر است؟', feeling)

    showfeeling = (True , False)
    showfeeling = st.selectbox('آیا کودک شما از خود احساس و هیجان نشان نمی دهد؟', showfeeling)

    age = st.slider('بازه سنی کودک خود را بر حسب ماه وارد کنید', 6.0, 100., 9.0)

    button = st.button('معاینه و تشخیص')
    if button:
        with st.chat_message("assistant"):
                with st.spinner('''درحال بررسی لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''بررسی انجام شد')
                    x = np.array([[calling, eye, simplegame, handy, joyshare, joyshow, recognize, otherkids,
                                   imagination, social, repeating, feeling, showfeeling, age]])

        y_prediction = model.predict(x)
        if y_prediction == True:
            st.write("<h4 style='text-align: right; color: gray;'>بر اساس داده های وارد شده، کودک شما به اوتیسم خفیف مبتلا می باشد</h4>", unsafe_allow_html=True)
            st.write("<h5 style='text-align: right; color: gray;'>برای درمان فرزند خود به روانشناس مراجعه کنید</h5>", unsafe_allow_html=True)
        elif y_prediction == False:
            st.write("<h4 style='text-align: right; color: gray;'>بر اساس داده های وارد شده، کودک شما در سلامتی کامل می باشد</h4>", unsafe_allow_html=True)

show_page()
