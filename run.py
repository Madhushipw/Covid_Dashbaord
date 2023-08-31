from libraries import *
import streamlit as st

#style = "shiny"
#size = 64

# Format the source URL with the desired values
#img_src = f"https://flagsapi.com/{country_code}/{style}/{size}.png"

st.write('Madhushi Weerasinghe')

countries = ['Sri Lanka', 'United States', 'Japan', 'Turkey', 'Nepal']
data_types = ['cases',' deaths', 'recovered']

flag_code = {"Sri Lanka":"lk","United States":"us","Japan":"jp","Turkey":"tr","Nepal":"np"}

country = st.sidebar.selectbox('Pick up a country', countries)
days = st.sidebar.slider('days', min_value=1, max_value=90, step=1)

data_type = st.sidebar.multiselect('Pick data types', data_types)

#st.write(country)

#Total cases
total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))

total_df = pd.concat([total_cases, total_deaths, total_recoveries], axis=1).astype(int)

#Daily cases
daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))

daily_df = pd.concat([daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)

#Yesterday cases
yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

#yesterday_df = pd.concat([yesterday_cases, yesterday_deaths, yesterday_recoveries], axis=1).astype(int)

st.title('Covid-19 Visualization Dashboard')

st.metric('Selected country', country)


# Display the image 
st.image(f"https://flagcdn.com/80x60/{flag_code[country]}.png")

#To display the yesterday data
#st.metric('Yesterday cases', yesterday_cases)
#st.metric('Yesterday deaths', yesterday_deaths)
#st.metric('Yesterday recoveries', yesterday_recoveries)

col1,col2,col3 = st.columns(3)
col1.metric('Yesterday Cases',yesterday_cases)
col2.metric('Yesterday Deaths',yesterday_deaths)
col3.metric('Yesterday Recoveries ', yesterday_recoveries)

#To add a line chart
st.line_chart(daily_df)

#Add the link of a video that find from youtube, the below one is an example video
st.video('https://youtu.be/D9tTi-CDjDU') #To add a youtube video


