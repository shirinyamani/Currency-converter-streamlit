from constant import currencies
import streamlit as st
from main import get_exchange_rate, convert_currency


st.title(':currency_exchange: :money_with_wings: Currency Converter')

st.markdown(""" Welcome to Currency Converter! This app is converting the Currency Units below to the target units!""")

base_currency= st.selectbox('Select your base Currency:', currencies)
target_currancy = st.selectbox('To What?', currencies)

amount =st.number_input('Enter amount:', min_value=0, value=100)

if amount > 0 and base_currency and target_currancy:
    exhchange_rate = get_exchange_rate(base_currency=base_currency, 
                      target_currancy=target_currancy)
    
    if exhchange_rate:
        converted_amount = convert_currency(amount=amount, exchange_rate=exhchange_rate)
        st.success(f":white_check_mark: It is gonna be {amount:.3f} :dollar: in {target_currancy}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f'{amount:.3f}{base_currency}')
        col2.markdown("<h1 style='text-align: center; margin: 0; color: red;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f'{amount:.3f}{target_currancy}')
    else:
        st.error('Error fetching for exchange rate!')
