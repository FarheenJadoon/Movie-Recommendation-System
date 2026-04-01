import streamlit as st
import pandas as pd
import pickle as pkl

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movie_dict=pkl.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pkl.load(open('similarity.pkl','rb'))
selected_movie_name=st.selectbox('what movie you want to watch:' , movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
     st.write(i)
