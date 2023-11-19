import streamlit as st
import requests

st.title('Weather and Currency Exchange Information App')

st.header('Interactive Information Widgets')

st.subheader('Get Weather Information for a City')
user_city = st.text_input('Enter a city:')
if user_city:
    loading_message = st.empty()
    loading_message.text('Loading weather data...')
    response = requests.get(f"https://ix1kkllnhl.execute-api.eu-north-1.amazonaws.com/prod/myCityFunction?city={user_city}")
    # st.write('Response Status Code:', response.status_code)
    if response.status_code == 200:
        loading_message.success('Successfully fetched weather data')
        weather_data = response.json()

        temp_kelvin = weather_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        condition = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        st.metric(label="Temperature", value=f"{temp_celsius:.2f} °C")        
        st.write(f"Temperature: {temp_kelvin}°K")
        # st.write(f"Temperature: {temp_celsius:.2f}°C")
        st.write(f"Condition: {condition}")
        st.write(f"Humidity: {humidity}%")
    else:
        loading_message.error('Failed to retrieve weather data')
        # st.error('Failed to retrieve weather data')


st.header('Static Weather Information')
static_city = "Limassol"  # Example city
api_key = "2ebd046c30d2ce5367dc69e2ea8b1ace"  # Replace with your OpenWeatherMap API key

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={static_city}&appid={api_key}&units=metric"  # units=metric for Celsius

response = requests.get(weather_url)

if response.status_code == 200:
    weather_data = response.json()

    temp_celsius_static = weather_data['main']['temp']  # Temperature is already in Celsius due to units=metric
    condition_static = weather_data['weather'][0]['description']
    humidity_static = weather_data['main']['humidity']

    st.write(f"Weather information for {static_city}:")
    st.metric(label="Temperature", value=f"{temp_celsius_static} °C")
    st.write(f"Condition: {condition_static}")
    st.write(f"Humidity: {humidity_static}%")
else:
    st.error('Failed to retrieve weather data for the static city')

# Static Currency Exchange Rates Widget
st.header('Static Exchange Rates: USD to EUR, JPY, GBP')
exchange_url = 'https://openexchangerates.org/api/latest.json?app_id=1722041c5158478381ff3a2f46768640'
exchange_response = requests.get(exchange_url)

if exchange_response.status_code == 200:
    exchange_data = exchange_response.json()

    # Extracting specific data
    usd_to_eur = exchange_data['rates']['EUR']
    usd_to_jpy = exchange_data['rates']['JPY']
    usd_to_gbp = exchange_data['rates']['GBP']

    # Displaying the extracted data
    st.write('USD to EUR:', usd_to_eur)
    st.write('USD to JPY:', usd_to_jpy)
    st.write('USD to GBP:', usd_to_gbp)
else:
    st.error('Failed to retrieve exchange rates')


# User input for currency information
st.subheader('Currency Conversion')
base_currency = st.selectbox('Select the base currency:', ('USD', 'JPY', 'GBP', 'EUR'))
target_currencies = st.multiselect('Select the target currencies:', ('USD', 'JPY', 'GBP', 'EUR'), default=['EUR'])

if base_currency and target_currencies:
    response = requests.get(f"https://paubxswj4j.execute-api.eu-north-1.amazonaws.com/default/myCurrencyFunction?base={base_currency}&targets={','.join(target_currencies)}")
    if response.status_code == 200:
        currency_data = response.json()

        # Extracting the rates
        rates = currency_data.get('rates', {})

        # Display the exchange rates
        st.write(f"Exchange rates for {base_currency}:")
        for target, rate in rates.items():
            st.write(f"{base_currency} to {target}: {rate}")
    else:
        st.error('Failed to retrieve currency data')
