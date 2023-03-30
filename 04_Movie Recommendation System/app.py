import streamlit as st
import pandas as pd
import pickle
import requests

def get_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def get_popularity(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return data['popularity']

def recommend(movie):
    movie_idx = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_idx]
    recomendations = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:11]

    recommended_movies = []
    recommeded_movies_posters=[]
    recommended_movies_popularity=[]
    for i in recomendations:
        id = movies_list['movie_id'][i[0]]
        recommended_movies.append(movies_list['title'][i[0]])
        recommeded_movies_posters.append(get_poster(id))
        recommended_movies_popularity.append(get_popularity(id))
    return recommended_movies,recommeded_movies_posters,recommended_movies_popularity


movies_list = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pd.DataFrame(movies_list)
st.title('Movie Recommendation System')
selected_movie_name = st.selectbox("Type a Movie Name",movies_list['title'].values)

recomedaton_btn = st.button("Get Recommendation")
if recomedaton_btn:
    #recommend(selected_movie_name)
    recommendations,posters,popularities = recommend(selected_movie_name)
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
            st.text(f'popularity {popularities[i+d]}')
            st.image(posters[i+d]) 
        with cols[i+d+1]:
            st.header(recommendations[i+d+1])
            st.text(f'popularity {popularities[i+d+1]}')
            st.image(posters[i+d+1]) 
        d+=1


   
    