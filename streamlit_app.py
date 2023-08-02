
import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My KPOP Library')

streamlit.header('WOODZ')
streamlit.text('06.2020 - EQUAL')
streamlit.text('11.2020 - WOOPS')
streamlit.text('03.2021 - SET')
streamlit.text('10.2021 - Only Lovers Left')
streamlit.text('04.2022 - Colorful Trauma')
streamlit.text('04.2023 - OO-LI 🥭')

streamlit.header('KEY')
streamlit.text('09.2021 - Bad Love')
streamlit.text('08.2022 - Gasoline 🍇')

streamlit.header('Fruit Smoothie')
streamlit.dataframe(my_fruit_list)
