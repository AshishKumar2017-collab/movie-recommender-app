# # why streamlit and flask?
# import pandas as pd
# import streamlit as st
# import pickle
# movie_list_dict=pickle.load(open('movies_dict.pkl','rb'))
# movies=pd.DataFrame(movie_list_dict)
# similarity=pickle.load(open('similarity.pkl','rb'))
#
# st.title ('Movies Recommendation System')
#
# # how to add text box where user will type?
# # option = st.selectbox(
# #     "How would you like to be contacted?",
# #     ("Email", "Home phone", "Mobile phone"),
# # )
# # now i want to feed data from to this ibrary so that i can use that?
# # to show movies list
# # so first need data of movies list
# # import pkl
# # movie_list=pickle.load(open('movies.pkl','rb'))
# # movie_list=movie_list['title'].value
#
# # option = st.selectbox(
# #     "How would you like to be contacted?",
# #     movie_list,
# # )
# # why the above code was not working what is other option to do it?
#
# # rather then dataframe sending just take list and then alll function written in notebook?
# # import pandas as pd
# # movie_list_dict=pickle.load(open('movies_dict.pkl','rb'))
# # movies=pd.DataFrame(movie_list_dict)
#
# option = st.selectbox(
#     "How would you like to be contacted?",
#     movies['title'].values
# )
#
# # line number 18 was incorrect?
#
# # now adding one button to recommend
# # if st.button('Recommend'):
# #     st.write('why hello there')
#
# #
# # if st.button('Recommend'):
#     # st.write(option)
# # similarity=pickle.load(open('similarity.pkl','rb'))
# def  recommend(movie):
#     movie_index=movies[movies['title']==movie].index[0]
#     distances=similarity[movie_index]
#     movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies=[]
#     for i in movie_list:
#         # print(i[0])`
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
#
#
#
# if st.button('Recommend'):
#     recommendation=recommend(option)
#     for i in recommendation:
#         st.write(i)
#



import pandas as pd
import streamlit as st
import pickle

def  recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in  movie_list :
        # print(i[0])`
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title ('Movies Recommendation System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)

if len(similarity) != len(movies):
    st.error("The similarity matrix dimensions do not match the movies dataset.")

print(movies.shape)  # Prints (number_of_rows, number_of_columns)
print(similarity.shape)  # Prints (number_of_rows, number_of_columns)
