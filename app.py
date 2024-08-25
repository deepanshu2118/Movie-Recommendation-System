import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    respone=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=396565f3b9dd7630e6369e672f55187f&language=en-US".format(movie_id))
    data=respone.json()
    return "http://image.tmdb.org/t/p/w500"+ data['poster_path']



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x : x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_recommend\movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('movie_recommend\similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movies_name=st.selectbox('hello',movies['title'].values)

if st.button('Recommend'):
    name,posters = recommend(selected_movies_name)

    col1,col2,col3,col4,col5 =st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])

    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])
