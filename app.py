import streamlit as st
import requests

# Title for the app
st.title('Weather and Currency Exchange Information App')

# ... [static widgets code] ...

# Interactive widgets for user-provided information
st.header('Interactive Information Widgets')

# User input for weather information
st.subheader('Get Weather Information for a City')
user_city = st.text_input('Enter a city:')
if user_city:
    response = requests.get(f"https://ix1kkllnhl.execute-api.eu-north-1.amazonaws.com/prod/myCityFunction?city={user_city}")
    st.write('Response Status Code:', response.status_code)
    if response.status_code == 200:
        weather_data = response.json()

        # Extracting specific data
        temp_kelvin = weather_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        condition = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        # Displaying the extracted data
        st.write(f"Weather information for {user_city}:")
        st.write(f"Temperature: {temp_kelvin}°K")
        st.write(f"Temperature: {temp_celsius:.2f}°C")
        st.write(f"Condition: {condition}")
        st.write(f"Humidity: {humidity}%")
    else:
        st.error('Failed to retrieve weather data')


# User input for currency information
st.subheader('Currency Conversion')
base_currency = st.selectbox('Select the base currency:', ('USD', 'JPY', 'GBP', 'EUR'))
target_currencies = st.multiselect('Select the target currencies:', ('USD', 'JPY', 'GBP', 'EUR'), default=['EUR'])

if base_currency and target_currencies:
    # Replace with your serverless function endpoint
    response = requests.get(f"https://paubxswj4j.execute-api.eu-north-1.amazonaws.com/default/myCurrencyFunction?base={base_currency}&targets={','.join(target_currencies)}")
    if response.status_code == 200:
        currency_data = response.json()
        st.write('Exchange rates for', base_currency, ':', currency_data)
    else:
        st.error('Failed to retrieve currency data')
