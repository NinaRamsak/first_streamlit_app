
import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # set the index by fruit and not numbers

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

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
