import streamlit as st
import pickle as pk
import pandas as pd

def recommend(song_name):
    song_idx = song_list[song_list['Song-Name']==song_name].index[0]
    distance = similarity[song_idx]
    recommendations = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]
    return recommendations

song_list = pk.load(open('sonds.pkl','rb'))
similarity = pk.load(open('similarity.pkl','rb'))
song_list = pd.DataFrame(song_list)
st.title("Song recommendation system collection of 2000-2500 Bollywood songs")
song_name = st.selectbox("enter a song name",song_list['Song-Name'])

if st.button('Recommend'):
    recommendations = recommend(song_name) 
    st.title("Top-5 Recommend Songs")
    for i in recommendations:
        st.text(song_list['Song-Name'][i[0]])