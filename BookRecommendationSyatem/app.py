import streamlit as st
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
import wikipedia

def get_image_link_from_id(id):
    link = f'https://en.wikipedia.org/w/index.php?curid={id}'
    return link

def recommend(book):
    wiki_book_link=[]
    final_recommendations=[]
    book_idx = books[books['book_title']==book].index[0]
    ds = similarity[book_idx]
    recommendations = sorted(list(enumerate(ds)),reverse=True,key = lambda x:x[1])[1:11]
    for i in recommendations:
        index=i[0]
        final_recommendations.append(books['book_title'][index])
        wiki_book_link.append(get_image_link_from_id(books['wiki_book_id'][index]))
    return final_recommendations , wiki_book_link


st.title('Book Recommendation System')
books = pickle.load(open('books.pkl','rb'))
books = pd.DataFrame(books)
similarity = pickle.load(open('similarity.pkl','rb'))

selected_book_name = st.selectbox("Enter a Book Name",books['book_title'].values)
recommend_button = st.button("Recommend Books")

if recommend_button:
    recommendations , links = recommend(selected_book_name)
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
    col5,col6 = st.columns(2)
    col7,col8 = st.columns(2)
    col9,col10 = st.columns(2)
    cols=[col1,col2,col3,col4,col5,col6,col7,col8,col9,col10]
    d=0
    for i in range(5):
        with cols[i+d]:
            st.header(recommendations[i+d])
            link = links[i+d]
            st.markdown(f"<a href='{link}'>Know More<a>", unsafe_allow_html=True)
        with cols[i+d+1]:
            st.header(recommendations[i+d+1])
            link = links[i+d+1]
            st.markdown(f"<a href='{link}'>Know More<a>", unsafe_allow_html=True)
        d+=1